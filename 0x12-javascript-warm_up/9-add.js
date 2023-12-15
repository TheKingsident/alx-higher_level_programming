#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const firstArgument = parseInt(process.argv[2], 10);
const secondArgument = parseInt(process.argv[3], 10);

console.log(add(firstArgument, secondArgument));
