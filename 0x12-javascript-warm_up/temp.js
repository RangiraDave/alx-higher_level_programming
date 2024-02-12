#!/usr/bin/node
// 4 2 5 3 0 -3 6 7

let max = process.argv[2];
let sec = process.argv[2];
for (let i = 2; i < process.argv.length; i++) {
  if (process.argv[i] >= max) {
    max = process.argv[i];
  } else {
    continue;
  }
  if (max > process.argv[i] && process.argv[i] >= sec) {
    sec = process.argv[i];
  } else {
    continue;
  }
}

console.log(max);
console.log('\n', sec);
