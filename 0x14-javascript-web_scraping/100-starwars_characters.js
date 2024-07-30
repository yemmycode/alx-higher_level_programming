#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node <script-file> <ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const movieApiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(movieApiUrl, (err, res, movieData) => {
  if (err) {
    console.error('Request error:', err);
    process.exit(1);
  }

  try {
    const movie = JSON.parse(movieData);
    movie.characters.forEach((charUrl) => {
      request.get(charUrl, (err, res, charData) => {
        if (err) {
          console.error('Request error:', err);
          process.exit(1);
        }
        const character = JSON.parse(charData);
        console.log(character.name);
      });
    });
  } catch (err) {
    console.error('Error parsing JSON:', err);
    process.exit(1);
  }
});
