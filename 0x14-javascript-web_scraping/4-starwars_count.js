#!/usr/bin/node

const request = require('request');

const baseURL = process.argv[2];
const characterID = 18;
let characterCount = 0;

function checkCharacterInMovie (movieId) {
  return new Promise((resolve, reject) => {
    const fullUrl = `${baseURL}/${movieId}`;

    request(fullUrl, { json: true }, (err, res, body) => {
      if (err) {
        reject(err);
        return;
      }

      if (!body || !body.characters) {
        resolve(false);
        return;
      }

      const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterID}/`;
      if (body.characters.includes(characterUrl)) {
        resolve(true);
      } else {
        resolve(false);
      }
    });
  });
}

async function main () {
  try {
    for (let movieId = 1; movieId <= 7; movieId++) {
      const hasCharacter = await checkCharacterInMovie(movieId);
      if (hasCharacter) {
        characterCount++;
      }
    }

    console.log(`${characterCount}`);
  } catch (error) {
  }
}

main();
