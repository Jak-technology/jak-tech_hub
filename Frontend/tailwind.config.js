/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./*.html", "./*.js'],
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    extend: {
      colors: {
        brightRed: 'hsl(12, 88%, 59%)',
        darkBlue: 'hsl(228, 39%, 23%)',
        darkGrayBlue: 'hsl(227, 12%, 61%)',
        veryDarkBlue: 'hsl(233, 12%, 13%)',
        veryPaleRed: 'hsl(13, 100%, 96%)',
        veryLightGray: 'hsl(0, 0%, 98%)',
        brightRedSuperLight: 'hsl(12, 100%, 95%)',
        brightRedLight: 'hsl(12, 100%, 72%)',
        lightBlue: 'hsl(228, 28%, 77%)',
      }
    },
  },
  plugins: [],
}

