import React from 'react';

const Home = () => {
    const toggleDarkMode = () => {
        document.documentElement.classList.toggle('dark');
        };
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex flex-col items-center justify-center px-4">
      <div className="max-w-2xl w-full bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-md text-center">
        <button onClick={toggleDarkMode}
            className="mb-6 px-4 py-2 text-sm bg-gray-300 dark:bg-gray-700 text-gray-800 dark:text-white rounded hover:bg-gray-400 dark:hover:bg-gray-600 transition"
            >
            Toggle Dark Mode
        </button>

        <h1 className="text-3xl font-bold text-gray-800 dark:text-white mb-4">Welcome to SCQWeb</h1>
        <p className="text-gray-600 dark:text-gray-300 text-lg">
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
            className="px-6 py-3 bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-100 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600 transition"
          >
            Learn More
          </a>
        </div>
      </div>
    </div>
  );
};

export default Home;
