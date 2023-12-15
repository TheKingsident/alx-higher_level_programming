#!/usr/bin/node

const argumentCo = process.argv.slice(2);

if (argumentCo.length === 0) {
  console.log('No argument');
} else if (argumentCo === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
