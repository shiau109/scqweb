import React, { useState, useEffect } from 'react';  
import ReactMarkdown from 'react-markdown';  
import remarkGfm    from 'remark-gfm';            // GFM: tables, task lists, strikethroughs :contentReference[oaicite:7]{index=7}  
import rehypeRaw    from 'rehype-raw';            // parse embedded HTML :contentReference[oaicite:8]{index=8}  
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';  
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism'; // theme :contentReference[oaicite:9]{index=9}

function Markdown({ url }) {
  const [content, setContent] = useState('');

  useEffect(() => {
    fetch(url)                                 // load .md file at runtime :contentReference[oaicite:10]{index=10}
      .then(res => res.text())
      .then(setContent);
  }, [url]);

  return (
    <ReactMarkdown
      children={content}
      remarkPlugins={[remarkGfm]}
      rehypePlugins={[rehypeRaw]}
      components={{
        code({node, inline, className, children, ...props}) {
          const match = /language-(\w+)/.exec(className || '');
          return !inline && match ? (
            <SyntaxHighlighter
              style={oneDark}
              language={match[1]}
              PreTag="div"
              {...props}
            >
              {String(children).replace(/\n$/, '')}
            </SyntaxHighlighter>
          ) : (
            <code className={className} {...props}>{children}</code>
          );
        }
      }}
    />
  );
}
export default Markdown;