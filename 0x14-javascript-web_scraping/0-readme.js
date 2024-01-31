#!/usr/bin/node

const filepath = process.argv[2];
const fs = require('fs');

fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
