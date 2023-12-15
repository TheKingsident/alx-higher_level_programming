#!/usr/bin/node

try {
  const firstArgument = process.argv[2];
  if (firstArgument === undefined) {
    throw new Error('No argument');
  }
  console.log(firstArgument);
} catch (error) {
  console.log('No argument');
}
