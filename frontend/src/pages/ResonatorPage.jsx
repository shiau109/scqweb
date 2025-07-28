import React, { useState, useEffect } from 'react';
import ResonatorForm from '../components/ResonatorForm';
import Markdown from '../components/Markdown';
import FileUploader from '../components/FileUploader';
import FileListSelector from '../components/FileListSelector';

function App() {
  const [files, setFiles] = useState([]);
  const [fileOptions, setFileOptions] = useState([]);
  const [error, setError] = useState('');
  const [plotImage, setPlotImage] = useState(null);

  // 🔄 Fetch file list after uploading or on load
  useEffect(() => {
    fetchFileList();
  }, []);

  const fetchFileList = async () => {
    try {
      const res = await fetch('http://localhost:8000/resonator/list');
      const data = await res.json();
      // initialize: not selected, default label = filename
      const enriched = data.map(f => ({
        name: f.name,
        selected: false,
        label: f.name.replace(/\.[^/.]+$/, "")  // strip extension
      }));
      setFileOptions(enriched);
    } catch (err) {
      console.error('Failed to fetch file list', err);
    }
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    files.forEach((file) => {
      formData.append('files', file);
    });

    try {
      const response = await fetch('http://localhost:8000/resonator/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const msg = await response.text();
        throw new Error(msg);
      }

      setFiles([]);
      setError('');
      fetchFileList(); // Refresh file list after upload
    } catch (error) {
      console.error('Upload error:', error);
      setError('Failed to upload files: ' + error.message);
    }
  };


  const handleRemoveFileFromBackend = async (filename) => {
    try {
      const res = await fetch('http://localhost:8000/resonator/remove', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ filename }),
      });

      if (!res.ok) {
        const err = await res.text();
        throw new Error(err);
      }

      // Remove from frontend state
      setFileOptions(fileOptions.filter(f => f.name !== filename));
    } catch (err) {
      console.error("Failed to remove file:", err);
      setError("Could not delete file: " + err.message);
    }
  };

  const handleGeneratePlot = async () => {
    const selectedFiles = fileOptions.filter(f => f.selected);
    if (selectedFiles.length === 0) {
      setError("Please select at least one file to plot.");
      return;
    }

    const payload = {
      files: selectedFiles.map(f => f.name),
      labels: selectedFiles.map(f => f.label || f.name),
    };

    try {
      const res = await fetch('http://localhost:8000/resonator/plot_group', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      if (!res.ok) throw new Error("Plot failed");

      const blob = await res.blob();
      const imageUrl = URL.createObjectURL(blob);
      setPlotImage(imageUrl);
      setError('');
    } catch (err) {
      console.error(err);
      setError("Failed to generate plot");
    }
  };

  return (
    <div className="App">
      <Markdown url="../../doc/MD/RF_resonator.md" />

      {/* Upload section */}
      <FileUploader
        files={files}
        setFiles={setFiles}
        onUpload={handleSubmit}
        error={error}
      />
      {/* Interactive file control section */}
      <FileListSelector
        fileOptions={fileOptions}
        setFileOptions={setFileOptions}
        onGenerate={handleGeneratePlot}
        onRemove={handleRemoveFileFromBackend}
      />

      {/* Plot Preview */}
      {plotImage && (
        <div className="my-6">
          <h3 className="font-semibold mb-2">Combined Resonator Plot:</h3>
          <img src={plotImage} alt="Resonator Plot" className="border rounded shadow" />
        </div>
      )}

      <ResonatorForm />
    </div>
  );
}

export default App;
