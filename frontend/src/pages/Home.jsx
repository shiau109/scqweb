import React from 'react';

const Home = () => {

  return (
    <div className="min-h-screen bg-gray-50  flex flex-col items-center justify-center px-4">
      <div className="max-w-2xl w-full bg-white  p-8 rounded-2xl shadow-md text-center">


        <h1 className="text-3xl font-bold text-gray-800 mb-4">Welcome to SCQWeb</h1>
        <p className="text-gray-600 text-lg">
          Explore and simulate superconducting qubit models with ease.
        </p>

        <div className="mt-8 flex flex-col sm:flex-row justify-center gap-4">
          <a
            href="/resonator"
            className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
          >
            Go to Resonator Tool
          </a>
          <a
            href="/about"
            className="px-6 py-3 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition"
          >
            Learn More
          </a>
        </div>
      </div>
    </div>
  );
};

export default Home;
