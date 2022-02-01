module.exports = {
  content: [
    './allauth_ui/templates/**/*.html',
  ],
  safelist: [
    { pattern: /social-|bg-/ }
  ],
  theme: {
    extend: {},
  },
  plugins: [
      /**
       * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
       * for forms. If you don't like it or have own styling for forms,
       * comment the line below to disable '@tailwindcss/forms'.
       */
      require('@tailwindcss/forms'),
      require('@tailwindcss/typography'),
      require('@tailwindcss/line-clamp'),
      require('@tailwindcss/aspect-ratio'),
  ],
}
