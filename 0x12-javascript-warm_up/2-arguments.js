#!/usr/bin/node

let argumentCo;

for (let i = 2; i < process.argv.length; i++) {
  argumentCo++;
}

if (argumentCo.length === 0) {
  console.log('No argument');
} else if (argumentCo === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
