#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
let characters = [];

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  characters = data.characters;
  fetchCharacterNames(0);
});

const fetchCharacterNames = (index) => {
  if (index === characters.length) {
    return;
  }

  request.get(characters[index], (err, res, body) => {
    if (err) {
      console.log(err);
      return;
    }

    const character = JSON.parse(body);
    console.log(character.name);
    fetchCharacterNames(index + 1);
  });
};
