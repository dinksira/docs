'use client';

import React, { useState, useRef, useCallback, useEffect } from "react";
import { useRouter } from "next/navigation";
import { useEditor, EditorContent } from "@tiptap/react";
import StarterKit from "@tiptap/starter-kit";
import { Color } from "@tiptap/extension-color";
import { TextStyle } from "@tiptap/extension-text-style";
import Highlight from "@tiptap/extension-highlight";
import UnderlineExt from "@tiptap/extension-underline";
import TextAlign from "@tiptap/extension-text-align";
import { Table } from "@tiptap/extension-table";
import { TableRow } from "@tiptap/extension-table-row";
import { TableCell } from "@tiptap/extension-table-cell";
import { TableHeader } from "@tiptap/extension-table-header";
import Youtube from "@tiptap/extension-youtube";
import Link from "@tiptap/extension-link";
import CodeBlockLowlight from "@tiptap/extension-code-block-lowlight";
import { common, createLowlight } from "lowlight";
import { ReactNodeViewRenderer } from "@tiptap/react";
import CodeBlockComponent from "./CodeBlockComponent";
import FloatingToolbar from "./FloatingToolbar";
import TurndownService from "turndown";
import { marked } from "marked";
import ResizableImage from "./ResizableImage";
import ResizableVideo from "./ResizableVideo";
import { pendingChanges } from "@/lib/pendingChanges";
import { draftStore } from "@/lib/draftStore";
import "./styles.css";

const lowlight = createLowlight(common);

const turndown = new TurndownService({
  headingStyle: "atx",
  codeBlockStyle: "fenced",
  bulletListMarker: "-",
});

turndown.keep(['span', 'mark', 'video', 'source', 'iframe', 'img', 'table', 'thead', 'tbody', 'tr', 'th', 'td']);

turndown.addRule('resizableImage', {
  filter: 'img',
  replacement: (content: string, node: Node) => {
    const img = node as HTMLImageElement;
    const src = img.getAttribute('src');
    const width = img.getAttribute('width');
    const align = img.getAttribute('align') || (img.style.display === 'block' ? (img.style.marginLeft === 'auto' ? 'right' : (img.style.margin === '0px auto' ? 'center' : 'left')) : 'left');
    
    if (width || align !== 'left') {
      let style = '';
      if (align === 'center') style = 'display: block; margin: 0 auto;';
      else if (align === 'right') style = 'display: block; margin-left: auto;';
      else style = 'display: block;';
      
      return `<img src="${src}" ${width ? `width="${width}"` : ''} style="${style}" />`;
    }
    
    return `![](${src})`;
  }
});



interface ChangeLogEntry {
  block_id: string;
  admin_name: string;
  admin_email: string;
  admin_avatar: string;
  edited_at: string;
  field: string;
}

interface RichEditorProps {
  content: string;
  slug: string;
  workspace?: string;
  blockId?: string;
  changeInfo?: ChangeLogEntry;
  onSaveSuccess?: (blockId: string, newValue: string) => void;
}
export default function RichEditor({
  content,
  slug,
  workspace = 'docs',
  blockId = "content",
  onSaveSuccess: _onSaveSuccess,
}: RichEditorProps) {
  const [isEditing, setIsEditing] = useState(false);
  const router = useRouter();
  const wrapperRef = useRef<HTMLDivElement>(null);
  const originalMarkdown = useRef(content);
  const currentMarkdown = useRef(content);

  // Handle portal-side navigation for internal links
  const handleContentClick = (e: React.MouseEvent) => {
    // If we're editing, we usually don't want to navigate on click (to allow cursor placement)
    // But if we're NOT editing, links should work like a real wiki
    if (isEditing) return;

    const target = e.target as HTMLElement;
    const anchor = target.closest('a');

    if (anchor && anchor.getAttribute('href')) {
      const href = anchor.getAttribute('href')!;
      
      // If it's a local portal link (starts with / or matches our workspace pattern)
      if (href.startsWith('/') || href.includes('workspace=')) {
        e.preventDefault();
        e.stopPropagation();
        
        // Construct the portal URL
        // Internal links are stored as slugs, e.g., /getting-started/intro
        // We need to route to /workspace/[slug]/page?slug=[slug]
        const cleanSlug = href.startsWith('/') ? href.slice(1) : href;
        router.push(`/workspace/${workspace}?slug=${cleanSlug}`);
      }
    }
  };

  // Switch to edit mode on double click or if specifically requested
  const handleDoubleClick = () => {
    if (!isEditing) {
      setIsEditing(true);
      setTimeout(() => {
        editor?.commands.focus();
      }, 50);
    }
  };

  const saveFn = useCallback(async () => {
    // We now use draftStore for centralized saving. 
    // This local saveFn is kept for backward compatibility with components 
    // expecting _onSaveSuccess, but the actual persistence happens in draftStore.
    _onSaveSuccess?.(blockId, currentMarkdown.current);
  }, [blockId, _onSaveSuccess]);

  const editor = useEditor({
    immediatelyRender: false,
    extensions: [
      StarterKit.configure({ 
        codeBlock: false,
        link: false,
        underline: false,
      }),
      Color,
      TextStyle,
      Highlight.configure({ multicolor: true }),
      UnderlineExt, // Keep these but we'll see if warning persists
      TextAlign.configure({ types: ["heading", "paragraph"] }),
      Table.configure({ 
        resizable: true,
        lastColumnResizable: true,
        handleWidth: 10, // Make handles easier to grab
      }),
      TableRow,
      TableHeader.extend({
        addAttributes() {
          return {
            ...this.parent?.(),
            backgroundColor: {
              default: null,
              parseHTML: element => element.style.backgroundColor || null,
              renderHTML: attributes => {
                if (!attributes.backgroundColor) return {};
                return { style: `background-color: ${attributes.backgroundColor}` };
              }
            }
          };
        }
      }),
      TableCell.extend({
        addAttributes() {
          return {
            ...this.parent?.(),
            backgroundColor: {
              default: null,
              parseHTML: element => element.style.backgroundColor || null,
              renderHTML: attributes => {
                if (!attributes.backgroundColor) return {};
                return { style: `background-color: ${attributes.backgroundColor}` };
              }
            }
          };
        }
      }),
      ResizableImage,
      ResizableVideo,
      Youtube.configure({ controls: true, nocookie: true }),
      Link.configure({ openOnClick: false }),
      CodeBlockLowlight.extend({
        addNodeView() {
          return ReactNodeViewRenderer(CodeBlockComponent)
        },
      }).configure({ lowlight }),
    ],
    editorProps: {
      handlePaste: (view, event) => {
        const text = event.clipboardData?.getData('text/plain');
        if (!text) return false;

        // Don't auto-parse if we're already inside a code block
        const isInsideCodeBlock = editor?.isActive('codeBlock');
        if (isInsideCodeBlock) return false;

        // Heuristic: Does it look like Markdown?
        const isMarkdown = /(^|\n)(#+ |[*_-]{2,}|> |[*+-] |\[.+\]\(.+\)|```)/.test(text);
        
        if (isMarkdown) {
          try {
            const html = marked.parse(text) as string;
            if (editor) {
              editor.commands.insertContent(html);
              return true;
            }
          } catch (e) {
            console.error("Markdown paste parsing failed:", e);
          }
        }
        return false;
      },
      attributes: {
        class: "rich-editor-content",
        spellcheck: "true",
      },
    },
    content: marked.parse(draftStore.getPage(slug, workspace) || content) as string,
    editable: false,
    onFocus: () => setIsEditing(true),
    onUpdate: ({ editor }) => {
      const html = editor.getHTML();
      const markdown = turndown.turndown(html);
      currentMarkdown.current = markdown;
      draftStore.savePage(slug, markdown, originalMarkdown.current, workspace);
    },
  });

  // Sync edit mode with tiptap engine
  useEffect(() => {
    if (editor) {
      editor.setEditable(isEditing);
    }
  }, [editor, isEditing]);

  // MS Word Style Table Resizing Logic
  useEffect(() => {
    if (!editor) return;

    const handleMouseDown = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      // Check if clicking near the bottom-right corner handle of the last cell
      const cell = target.closest('td, th');
      if (!cell) return;
      
      const table = cell.closest('table');
      if (!table) return;

      const isLastCell = cell.parentElement?.nextElementSibling === null && cell.nextElementSibling === null;
      if (!isLastCell) return;

      const rect = cell.getBoundingClientRect();
      const isCorner = (e.clientX > rect.right - 15) && (e.clientY > rect.bottom - 15);

      if (isCorner) {
        e.preventDefault();
        e.stopPropagation();

        const startX = e.clientX;
        const startWidth = table.offsetWidth;

        const onMouseMove = (me: MouseEvent) => {
           const deltaX = me.clientX - startX;
           const newWidth = Math.max(100, startWidth + deltaX);
           table.style.width = `${newWidth}px`;
           table.style.minWidth = `${newWidth}px`; // Force override
        };

        const onMouseUp = () => {
           document.removeEventListener('mousemove', onMouseMove);
           document.removeEventListener('mouseup', onMouseUp);
           // After global resize, we might want to update tiptap attributes,
           // but for simple visual preview, styling the element works well.
        };

        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);
      }
    };

    const dom = editor.options.element;
    if (!dom || !(dom instanceof HTMLElement)) return;

    const handleMouseMove = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      const table = target.closest('table');
      if (!table) return;

      const rect = table.getBoundingClientRect();
      const edgeThreshold = 30; // pixels from edge

      // check if near bottom edge
      if (e.clientY > rect.bottom - edgeThreshold && e.clientY < rect.bottom + edgeThreshold) {
         // show add row button... (logic simplified for brevity, will use CSS handles)
      }
    };

    // Use capture phase (true) to ensure our global resize handle catches the event 
    // before Tiptap's internal selection logic
    dom.addEventListener('mousedown', handleMouseDown, true);
    dom.addEventListener('mousemove', handleMouseMove);
    return () => {
      dom.removeEventListener('mousedown', handleMouseDown, true);
      dom.removeEventListener('mousemove', handleMouseMove);
    };
  }, [editor]);

  // Enable editing on click
  function handleClick() {
    if (!editor || isEditing) return;
    editor.setEditable(true);
    editor.commands.focus();
    setIsEditing(true);
  }

  const lastSlug = useRef(slug);

  useEffect(() => {
    if (!editor) return;
    
    if (lastSlug.current !== slug || (!isEditing && content !== originalMarkdown.current)) {
      const draft = draftStore.getPage(slug, workspace);
      const effectiveContent = draft !== null ? draft : content;
      
      const newHtml = marked.parse(effectiveContent) as string;
      originalMarkdown.current = content;
      currentMarkdown.current = effectiveContent;
      
      editor.commands.setContent(newHtml);
      editor.setEditable(false);
      
      // Use setTimeout to avoid cascading render warning and ensure logic doesn't loop
      if (isEditing) {
        setTimeout(() => setIsEditing(false), 0);
      }
      lastSlug.current = slug;
      
      if (draft !== null && draft !== content) {
        pendingChanges.registerChange("page", `${slug}:${blockId}`, saveFn, workspace);
      }
    }
  }, [content, slug, editor, isEditing, blockId, saveFn]);

  useEffect(() => {
    const handleGlobalMouseDown = (e: MouseEvent) => {
      if (wrapperRef.current?.contains(e.target as Node)) return;
      const target = e.target as HTMLElement;
      if (target.closest('[data-floating-toolbar="true"]')) return;
      if (isEditing) {
        setIsEditing(false);
        editor?.commands.blur();
        editor?.setEditable(false);
      }
    };
    document.addEventListener('mousedown', handleGlobalMouseDown);
    return () => document.removeEventListener('mousedown', handleGlobalMouseDown);
  }, [isEditing, editor]);

  function handleCancel() {
    if (!editor) return;
    const originalHtml = marked.parse(originalMarkdown.current) as string;
    editor.commands.setContent(originalHtml);
    editor.setEditable(false);
    setIsEditing(false);
    pendingChanges.removeChange("page", `${slug}:${blockId}`, workspace);
  }

  function handleKeyDown(e: React.KeyboardEvent) {
    if (e.key === "Escape") {
      handleCancel();
    }
  }

  return (
    <div
      ref={wrapperRef}
      className={`rich-editor-wrapper ${isEditing ? "is-editing" : ""}`}
      onKeyDown={handleKeyDown}
    >
      {/* Floating toolbar — now rendered outside the content container */}
      {isEditing && <FloatingToolbar editor={editor} workspace={workspace} />}

      <div
        className="rich-editor-content-container"
        onClick={handleContentClick}
        onDoubleClick={handleDoubleClick}
        style={{ cursor: isEditing ? "text" : "pointer", position: "relative" }}
      >
        {!isEditing && (
           <div className="editor-hover-hint">
             ✏️ Content Modification Mode
           </div>
        )}
        <EditorContent editor={editor} />
      </div>
    </div>
  );
}
