#!/usr/bin/node
// Script to read and display contend from a file

const fs = require('fs');

function writeFileContent (filename, content) {
  fs.appendFile(filename, content, 'utf-8', (err) => {
    if (err) {
      console.error(`${err}`);
    }
  });
}

const filename = process.argv[2];
const content = process.argv[3];
writeFileContent(filename, content);
