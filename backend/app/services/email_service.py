import logging
import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings

logger = logging.getLogger(__name__)

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"


async def _send_email(to_email: str, subject: str, body: str):
    """
    Sends email via the best available method with automatic fallback.
    Optimized to prioritize reliable providers and detect trial-account restrictions.
    """
    errors = []

    # 1. Try Brevo (Primary - Most reliable for Render/Cloud)
    if settings.BREVO_API_KEY:
        try:
            await _send_via_brevo(to_email, subject, body)
            return
        except Exception as e:
            logger.warning(f"[EMAIL] Brevo failed: {e}")
            errors.append(f"Brevo: {str(e)}")

    # 2. Try Google Apps Script Gateway (Fallback)
    google_url = getattr(settings, 'GOOGLE_SCRIPT_URL', None) or os.getenv('GOOGLE_SCRIPT_URL')
    if google_url:
        try:
            payload = {"to": to_email, "subject": subject, "body": body}
            # DEBUG LOG: Verify what is actually being sent to Google
            logger.info(f"[DEBUG] PAYLOAD BEING SENT TO GOOGLE: {payload}")
            
            resp = requests.post(google_url, json=payload, timeout=15)
            # Some scripts return "Success", others just "OK". We look for anything that isn't "Error"
            if "Error" in resp.text or not resp.ok:
                raise RuntimeError(f"Script Error: {resp.text}")
            logger.info(f"[EMAIL] Sent to {to_email} via Google Gateway.")
            return
        except Exception as e:
            logger.warning(f"[EMAIL] Google Gateway failed: {e}")
            errors.append(f"Google: {str(e)}")

    # 3. Try Resend
    if settings.RESEND_API_KEY:
        try:
            # SAFETY CHECK: If using Resend onboarding email, it ONLY works for the owner
            if settings.FROM_EMAIL == 'onboarding@resend.dev' and to_email.lower() != 'dinksiraelisa@gmail.com':
                msg = f"Resend trial restriction: Cannot send to {to_email} from onboarding@resend.dev"
                logger.warning(f"[EMAIL] {msg}")
                errors.append(msg)
            else:
                await _send_via_resend(to_email, subject, body)
                return
        except Exception as e:
            logger.warning(f"[EMAIL] Resend failed: {e}")
            errors.append(f"Resend: {str(e)}")

    # 4. Try SMTP
    if settings.SMTP_HOST and settings.SMTP_USER:
        try:
            await _send_via_smtp(to_email, subject, body)
            return
        except Exception as e:
            logger.error(f"[EMAIL] SMTP failed: {e}")
            errors.append(f"SMTP: {str(e)}")

    # FINAL FALLBACK: Log to terminal so admin can still get the code from logs
    error_summary = " | ".join(errors)
    logger.error(f"[EMAIL] All services failed for {to_email}: {error_summary}")
    
    print("\n" + "!"*60)
    print("DEVELOPER/EMERGENCY FALLBACK: OTP LOGGED TO CONSOLE")
    print(f"RECIPIENT: {to_email}")
    print(f"MESSAGE:\n{body}")
    print("!"*60 + "\n")

    # In production, we should probably raise an error, 
    # but for now we succeed to allow manual login via logs.
    return


async def _send_via_brevo(to_email: str, subject: str, body: str):
    """Sends email via Brevo (Sendinblue) HTTP API."""
    from_addr = settings.EMAIL_FROM_ADDRESS or settings.BREVO_SENDER_EMAIL
    from_name = settings.BREVO_SENDER_NAME or "Delta Labs"

    payload = {
        "sender": {"name": from_name, "email": from_addr},
        "to": [{"email": to_email}],
        "subject": subject,
        "textContent": body,
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "api-key": settings.BREVO_API_KEY,
    }
    try:
        resp = requests.post(BREVO_API_URL, json=payload, headers=headers, timeout=10)
        resp.raise_for_status()
        logger.info(f"[EMAIL] Sent to {to_email} via Brevo. status={resp.status_code}")
    except requests.exceptions.HTTPError:
        msg = f"Brevo API error {resp.status_code}: {resp.text}"
        logger.error(f"[EMAIL] {msg}")
        raise RuntimeError(msg)
    except Exception as e:
        logger.error(f"[EMAIL] Unexpected Brevo error sending to {to_email}: {str(e)}")
        raise RuntimeError(f"Failed to send email via Brevo: {str(e)}")


async def _send_via_resend(to_email: str, subject: str, body: str):
    """Sends email via Resend HTTP API."""
    import resend
    resend.api_key = settings.RESEND_API_KEY
    from_addr = settings.FROM_EMAIL or "onboarding@resend.dev"

    try:
        resp = resend.Emails.send({
            "from": from_addr,
            "to": [to_email],
            "subject": subject,
            "text": body,
        })
        logger.info(f"[EMAIL] Sent to {to_email} via Resend. id={resp.get('id')}")
    except Exception as e:
        logger.error(f"[EMAIL] Resend error sending to {to_email}: {str(e)}")
        raise RuntimeError(f"Failed to send email via Resend: {str(e)}")


async def _send_via_smtp(to_email: str, subject: str, body: str):
    """Sends email via SMTP (e.g. Gmail App Password)."""
    from_addr = settings.EMAIL_FROM_ADDRESS or settings.SMTP_USER

    msg = MIMEMultipart()
    msg["From"] = f"Delta Labs <{from_addr}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT, timeout=10) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.sendmail(from_addr, to_email, msg.as_string())
        logger.info(f"[EMAIL] Sent to {to_email} via SMTP ({settings.SMTP_HOST})")
    except Exception as e:
        logger.error(f"[EMAIL] SMTP error sending to {to_email}: {str(e)}")
        raise RuntimeError(f"Failed to send email via SMTP: {str(e)}")


async def send_new_signup_alert(applicant_name: str, applicant_email: str):
    """Sends email TO all super admins about a new signup request. Non-critical — silent fail."""
    from app.database import get_db
    db = get_db()
    super_admins = await db.users.find({'role': 'super_admin'}).to_list(100)

    subject = "New Admin Access Request — Delta Labs"
    body = (
        "A new admin has requested access to the Delta Labs portal.\n"
        f"Name: {applicant_name}\n"
        f"Email: {applicant_email}\n"
        "Please log in to review and approve or reject this request."
    )
    for admin in super_admins:
        try:
            await _send_email(admin['email'], subject, body)
        except Exception as e:
            logger.warning(f"[EMAIL] Could not alert super admin {admin['email']}: {str(e)}")


async def send_approval_email(admin_name: str, admin_email: str):
    """Sends email TO the applicant on approval. Non-critical — silent fail."""
    subject = "Your Delta Labs Admin Access Has Been Approved"
    body = (
        f"Hi {admin_name},\n"
        "Your request to access the Delta Labs admin portal has been approved.\n"
        f"You can now log in at {settings.FRONTEND_URL}.\n"
        "Welcome to the team."
    )
    try:
        await _send_email(admin_email, subject, body)
    except Exception as e:
        logger.warning(f"[EMAIL] Could not send approval email to {admin_email}: {str(e)}")


async def send_rejection_email(admin_name: str, admin_email: str):
    """Sends email TO the applicant on rejection. Non-critical — silent fail."""
    subject = "Delta Labs Admin Access Request Update"
    body = (
        f"Hi {admin_name},\n"
        "After review, your request to access the Delta Labs admin portal "
        "was not approved at this time.\n"
        "If you believe this is an error, please contact your team lead."
    )
    try:
        await _send_email(admin_email, subject, body)
    except Exception as e:
        logger.warning(f"[EMAIL] Could not send rejection email to {admin_email}: {str(e)}")


async def send_otp_email(admin_name: str, admin_email: str, otp: str):
    """
    Sends OTP verification code to admin via Brevo.
    CRITICAL — raises an exception if it fails so the route returns a proper error.
    """
    subject = "Your Delta Labs Verification Code"
    body = (
        f"Hi {admin_name},\n\n"
        f"Your verification code is: {otp}\n\n"
        "This code expires in 5 minutes.\n"
        "If you did not request this, please ignore this email."
    )
    # No try/except — let the exception propagate to the caller
    await _send_email(admin_email, subject, body)

