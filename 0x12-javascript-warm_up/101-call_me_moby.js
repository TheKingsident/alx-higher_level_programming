#!/usr/bin/node

function executeXTimes (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

if (typeof module !== 'undefined') {
  module.exports = { executeXTimes };
}
