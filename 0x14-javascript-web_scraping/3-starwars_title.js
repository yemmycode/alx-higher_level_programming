#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node <script-file> <ID>');
  process.exit(1);
}

const [movieId] = process.argv.slice(2);
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (err, res, data) => {
  if (err) {
    console.error('Request error:', err);
    process.exit(1);
  }

  try {
    const movie = JSON.parse(data);
    console.log(movie.title);
  } catch (err) {
    console.error('JSON parsing error:', err);
    process.exit(1);
  }
});
