
const React = require('react')

module.exports = {
  beforeServiceStarts (done) {
    done({
      compiledDir: './js/components',
      port: 8181
    })
  },
  decorateComponent: (component, props) => (
    React.createElement(component, props)
  )
}
