import React from 'react';
import ResonatorForm from '../components/ResonatorForm';
import Markdown from '../components/Markdown';

function App() {
  return (
    <div className="App">
      <h1
        className="text-2xl font-extrabold tracking-tight text-gray-900">
        Resonator
      </h1> 
      <Markdown url="../../doc/MD/RF_resonator.md" />
      <ResonatorForm />
    </div>
  );
}

export default App;
