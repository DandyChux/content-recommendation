/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./**/templates/**/*.html'],
  mode: 'jit',
  content: [
    './**/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

