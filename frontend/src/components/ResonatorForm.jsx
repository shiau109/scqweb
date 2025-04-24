// src/components/ResonatorForm.js
import React, { useState } from 'react';

function ResonatorForm() {
  const [formData, setFormData] = useState({
    alpha: '',
    delay: '',
    Ql: '',
    Qc: '',
    phi: '',
    fr: '',
    freq_start: '',
    freq_end: '',
    freq_points: ''
  });
  const [imageSrc, setImageSrc] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const form = new FormData();
    for (const key in formData) {
      form.append(key, formData[key]);
    }

    try {
      const response = await fetch('http://localhost:8000/plot', {
        method: 'POST',
        body: form
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      setImageSrc(url);
    } catch (error) {
      console.error('Error fetching the plot:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input name="alpha" value={formData.alpha} onChange={handleChange} placeholder="Alpha" />
        <input name="delay" value={formData.delay} onChange={handleChange} placeholder="Delay" />
        <input name="Ql" value={formData.Ql} onChange={handleChange} placeholder="Ql" />
        <input name="Qc" value={formData.Qc} onChange={handleChange} placeholder="Qc" />
        <input name="phi" value={formData.phi} onChange={handleChange} placeholder="Phi" />
        <input name="fr" value={formData.fr} onChange={handleChange} placeholder="Fr" />
        <input name="freq_start" value={formData.freq_start} onChange={handleChange} placeholder="Frequency Start" />
        <input name="freq_end" value={formData.freq_end} onChange={handleChange} placeholder="Frequency End" />
        <input name="freq_points" value={formData.freq_points} onChange={handleChange} placeholder="Frequency Points" />
        <button type="submit">Generate Plot</button>
      </form>
      {imageSrc && <img src={imageSrc} alt="Resonator Response" />}
    </div>
  );
}

export default ResonatorForm;
