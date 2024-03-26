#!/usr/bin/node
// Script to display Star Wars movie title where the episode number maches given int

const request = require('request');

if (!process.argv[2]) {
  console.log('Please provide the episode number as argument');
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
