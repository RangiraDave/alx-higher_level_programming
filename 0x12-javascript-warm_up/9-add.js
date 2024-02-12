#!/usr/bin/node
// Function to return sum of two passed args.

function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
