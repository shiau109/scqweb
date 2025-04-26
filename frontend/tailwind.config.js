// ─────────────────────────────────────
// tailwind.config.js  (ESM)
// ─────────────────────────────────────
/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',    // if you’re still using dark mode
  content: [
    './index.html',
    './src/**/*.{js,jsx,ts,tsx}',
  ],
  theme: { extend: {} },
  plugins: [],
}
