/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'client/templates/client/*.html',
    'core/templates/core/*.html',
    'dashboard/templates/dashboard/*.html',
    'lead/templates/lead/*.html',
    'team/templates/team/*.html',
    'userprofile/templates/userprofile/*.html',
    './*.html',
    './assets/**/*.js'],
  theme: {
    extend: {},
  },
  plugins: [require("tailgrids/plugin")],
}

