'use client';

import React, { useState } from 'react';
import { NodeViewContent, NodeViewWrapper } from '@tiptap/react';
import { Copy, Check } from 'lucide-react';

export default function CodeBlockComponent({ node, updateAttributes, extension }: any) {
  const [copied, setCopied] = useState(false);

  const languages = extension.options.lowlight.listLanguages();

  const handleCopy = () => {
    const text = node.textContent;
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  console.log("🚀 CodeBlockComponent active for node:", node.attrs.language);

  return (
    <NodeViewWrapper className="code-block-wrapper group relative border-2 border-dashed border-blue-500/20 rounded-xl my-8">
      <div className="code-block-header absolute top-4 right-4 z-[9999] flex items-center gap-2">
        <button
          onClick={handleCopy}
          className={`flex items-center gap-1.5 px-3 py-2 rounded-lg text-[11px] font-black uppercase tracking-widest transition-all shadow-2xl active:scale-95
            ${copied 
              ? 'bg-emerald-500 text-white' 
              : 'bg-blue-600 text-white hover:bg-blue-500'}
          `}
        >
          {copied ? (
            <>
              <Check size={12} strokeWidth={3} />
              <span>Copied!</span>
            </>
          ) : (
            <>
              <Copy size={12} strokeWidth={2.5} />
              <span>Copy</span>
            </>
          )}
        </button>
      </div>
      
      <pre data-language={node.attrs.language}>
        <NodeViewContent as="code" />
      </pre>
    </NodeViewWrapper>
  );
}
