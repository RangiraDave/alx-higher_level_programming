#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const request = require('request');

if (!process.argv[2]) {
  console.log('Please provide the URL as an argument.');
  process.exit(1);
}

const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completed = {};

    tasks.forEach(task => {
      if (task.completed) {
        if (!completed[task.userId]) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    });

    console.log(completed);
  } else {
    console.log('An error occurred. Status code: ' + response.statusCode);
  }
});
