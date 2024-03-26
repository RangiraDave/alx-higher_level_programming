#!/usr/bin/node
// Script to print the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');

if (!process.argv[2]) {
  console.log('Please provide the URL as an argument.');
  process.exit(1);
}

const url = process.argv[2];
let movieCount = 0;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const movies = JSON.parse(body).results;
  const wedgeMovies = movies.filter(movie => {
    return movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18')
  });

  console.log(`${wedgeMovies.length}`);
});
