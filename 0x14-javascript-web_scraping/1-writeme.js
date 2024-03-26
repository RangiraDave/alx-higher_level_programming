#!/usr/bin/node
// Script to read and display contend from a file

const fs = require('fs');

function writeFileContent (filename) {
  fs.writeFile(filename, content, 'utf-8', (err) => {
    if (err) {
      console.error(`Error writing the file: ${err}`);
      return;
    }
  });
}

const filename = process.argv[2];
const content = process.argv[3];
if (!filename || !content) {
  console.error('Provide a file name and content as an argument.');
} else {
  writeFileContent(filename, content);
}
