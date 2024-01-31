#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    fs.writeFileSync(filepath, body, 'utf8');
  } catch (err) {
    console.error(err);
  }
});
