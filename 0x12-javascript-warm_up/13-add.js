#!/usr/bin/node

function add (a, b) {
  return a + b;
}

if (typeof module !== 'undefined') {
  module.exports = { add };
}
