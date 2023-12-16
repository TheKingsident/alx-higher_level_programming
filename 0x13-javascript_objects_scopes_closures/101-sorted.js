#!/usr/bin/node

const data = require('./101-data.js');
const dict = data.dict;

const occurrencesByUserId = {};

for (const [userId, occurrence] of Object.entries(dict)) {
  if (!occurrencesByUserId[occurrence]) {
    occurrencesByUserId[occurrence] = [];
  }
  occurrencesByUserId[occurrence].push(parseInt(userId));
}

console.log(occurrencesByUserId);
