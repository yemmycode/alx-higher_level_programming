#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';
let count = 0;

request.get(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const parsedData = JSON.parse(data);
    parsedData.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
