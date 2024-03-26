#!/usr/bin/node
// Script to print the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');

if (!process.argv[2]) {
  console.log('Please provide the URL as an argument.');
  process.exit(1);
}

const url = process.arv[2]
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log(process.count(JSON.parse(body['characterId']) === 18));
});
