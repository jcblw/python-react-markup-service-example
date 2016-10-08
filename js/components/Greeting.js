
const React = require('react')

const Greeting = ({ name }) => (
  React.createElement('h1', {}, `Hello ${name}!`)
)

module.exports = Greeting
