import React from 'react'
import { Link } from 'react-router-dom'

function App() {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-800 font-sans flex flex-col items-center justify-center p-8">
      <header className="text-center">
        <h1 className="text-4xl font-bold mb-4">🧪 Quantum Simulation GUI</h1>
        <p className="text-lg mb-6">Welcome! Use this tool to upload data, run simulations, and visualize results.</p>
      </header>

      <nav className="flex gap-4 mt-4">
        <Link to="/formula">
          <button className="px-4 py-2 bg-blue-600 text-white rounded shadow hover:bg-blue-700">
            Formula Calculator
          </button>
        </Link>
        <Link to="/resonator">
          <button className="px-4 py-2 bg-blue-600 text-white rounded shadow hover:bg-blue-700">
            Resonator
          </button>
        </Link>
      </nav>
    </div>
  )
}
export default App
