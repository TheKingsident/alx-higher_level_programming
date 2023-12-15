#!/usr/bin/node

function findSecondBiggest (args) {
  if (args.length < 2) {
    return 0;
  }

  const numbers = args.map(Number);
  const uniqueNumbers = [...new Set(numbers)];

  uniqueNumbers.sort((a, b) => b - a);

  return uniqueNumbers[1] || 0;
}

const args = process.argv.slice(2);
console.log(findSecondBiggest(args));
