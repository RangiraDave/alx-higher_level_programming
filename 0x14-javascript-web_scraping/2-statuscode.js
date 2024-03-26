#!/usr/bin/node
// Script to display status code of a GET request to a given url

const request = require('request');

if (!process.argv[2]) {
  console.log('Please provide a URL');
  process.exit(1);
}

const url = process.argv[2];
request(url, function (err, response) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
