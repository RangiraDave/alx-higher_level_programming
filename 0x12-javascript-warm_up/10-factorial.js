#!/usr/bin/node
// Script to create functorial.

function factorial (n) {
  if (!Number(process.argv[2]) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(Number(process.argv[2])));
