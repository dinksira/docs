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

  return (
    <NodeViewWrapper className="code-block-wrapper group/code relative">
      <div className="code-block-header absolute top-0 right-0 z-10 flex items-center gap-2 p-2 opacity-0 group-hover/code:opacity-100 transition-opacity">
        <button
          onClick={handleCopy}
          className={`flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-[10px] font-bold uppercase tracking-wider transition-all shadow-lg backdrop-blur-md
            ${copied 
              ? 'bg-emerald-500 text-white scale-105' 
              : 'bg-white/10 hover:bg-white/20 text-slate-300 border border-white/10'}
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
