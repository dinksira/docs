'use client';

import { GoogleOAuthProvider } from '@react-oauth/google';

export default function GoogleAuthProvider({ children }: { children: React.ReactNode }) {
  const clientId = process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID || '1012036745823-vtpb3p7dkvpkduserr8n51qhmsah5l1a.apps.googleusercontent.com';
  
  return (
    <GoogleOAuthProvider clientId={clientId}>
      {children}
    </GoogleOAuthProvider>
  );
}
