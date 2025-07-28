import React from 'react';

export default function FileUploader({ files, setFiles, onUpload, error }) {
  const handleFileChange = (e) => {
    const newFiles = Array.from(e.target.files);
    const validFiles = newFiles.filter(file => file.size <= 2048 * 1024);
    const tooLarge = newFiles.filter(file => file.size > 2048 * 1024);

    if (tooLarge.length > 0) {
      alert("Some files exceed 2MB and were not added.");
    }

    const updatedFiles = [...files];
    validFiles.forEach((file) => {
      if (!updatedFiles.find(f => f.name === file.name)) {
        updatedFiles.push(file);
      }
    });

    setFiles(updatedFiles);
    e.target.value = null;
  };

  return (
    <div className="my-4 p-4 border rounded bg-gray-50">
      <label className="block font-semibold mb-2">Upload files (each ≤ 2MB):</label>
      <input
        type="file"
        accept=".csv,.nc"
        multiple
        onChange={handleFileChange}
        className="block w-full text-sm text-gray-700"
      />
      {error && <p className="text-red-600 mt-2">{error}</p>}
      {files.length > 0 && (
        <ul className="mt-3 space-y-1">
          {files.map((file, idx) => (
            <li key={idx} className="flex justify-between items-center bg-white p-2 rounded shadow-sm">
              <span>{file.name} ({(file.size / 1024).toFixed(1)} KB)</span>
            </li>
          ))}
        </ul>
      )}
      {files.length > 0 && (
        <button
          onClick={onUpload}
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Submit Files
        </button>
      )}
    </div>
  );
}
