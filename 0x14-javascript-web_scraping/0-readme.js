#!/usr/bin/node
// Script to read and display contend from a file

const fs = require('fs');

function readFileContent (filename) {
  fs.readFile(filename, 'utf-8', (err, data) => {
    if (err) {
      console.error(`Error reading the file: ${err}`);
      return;
    }
    console.log(`${data}`);
  });
}

const filename = process.argv[2];
if (!filename) {
  console.error('Provide a file name as an argument.');
} else {
  readFileContent(filename);
}
