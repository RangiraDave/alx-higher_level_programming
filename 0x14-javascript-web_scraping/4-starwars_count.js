#!/usr/bin/node
// Script to print the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');

if (!process.argv[2]) {
  console.log('Please provide the URL as an argument.');
  process.exit(1);
}

const url = process.argv[2];
// const movieCount = 0;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const results = JSON.parse(body).results;
  console.log(results.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0));
});
