/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["../views/*.html"],
  theme: {
    fontSize: {
      '13': '13px',
      '14': '14px',
      '15': '15px',
      '17': '17px',
      '20': '20px',
      '23': '23px',
    },

    extend: {
      backdropBlur: {
        '3': '3px',
      },

      colors: {
        'twitter-search-bg': '#202327',
        'twitter-light-grey': '#e7e9ea',
        'twitter-grey': '#71767B',
        'twitter-dark-grey': '#0F1419',
        'twitter-dark-hover': '#181818', 
        'twitter-right-box-bg': '#16181C',
        'twitter-line': '#2F3336',
        'twitter-blue': '#1DA1F2',
        'twitter-green': '#19c981',
        'twitter-red': '#fd187d',
        'twitter-overlay': "#5B7085",
      },
      opacity: {
        '15': '.15',
      },
      transitionDuration: {
        '50': '50ms',
        '250': '250ms',
      },
      width: {
        '13': '0.813rem',
        '250': '15.625rem',
        '350': '21.875rem',
        '420': '26.25rem',
        '600': '37.5rem',
        '640': '40rem',
        '990': '61.875',
      },
      margin: {
        '18': '4.5'
      },
      padding: {
        '2.25': '9px',
      },
      boxShadow: {
        'search': '5px 5px 5px 5px rgb(231,233,234, 0.25)',
      },

      zIndex: {
        '100': '100',
      }
    },
  },
  plugins: [],
}