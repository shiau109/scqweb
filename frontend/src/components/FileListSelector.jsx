import React from 'react';

export default function FileListSelector({ fileOptions, setFileOptions, onGenerate, onRemove }) {
  const toggleFile = (index) => {
    const updated = [...fileOptions];
    updated[index].selected = !updated[index].selected;
    setFileOptions(updated);
  };

  const updateLabel = (index, label) => {
    const updated = [...fileOptions];
    updated[index].label = label;
    setFileOptions(updated);
  };

  return (
    <div className="my-6 p-4 border rounded bg-white shadow">
      <h3 className="font-semibold mb-2">Select Files to Plot:</h3>
      <ul className="space-y-2">
        {fileOptions.map((file, idx) => (
          <li key={idx} className="flex items-center gap-2">
            <input type="checkbox" checked={file.selected} onChange={() => toggleFile(idx)} />
            <span className="w-1/3 truncate">{file.name}</span>
            <input
              type="text"
              className="border px-2 py-1 rounded w-1/3"
              value={file.label}
              onChange={(e) => updateLabel(idx, e.target.value)}
              placeholder="Label for legend"
            />
            <button
              className="ml-auto text-red-600 hover:underline text-sm"
              onClick={() => onRemove(file.name)}
            >
              Remove
            </button>
          </li>
        ))}
      </ul>
      <button
        onClick={onGenerate}
        className="mt-4 bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
      >
        Generate Plot
      </button>
    </div>
  );
}
