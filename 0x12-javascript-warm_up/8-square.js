#!/usr/bin/node
// Script to print square accourding to the argv[2] passed.

if (!Number(process.argv[2])) {
  console.log('Missing size');
} else {
  let t = '';
  for (let i = 0; i < (process.argv[2]); i++) {
    t += 'X';
  }
  for (let j = 0; j < process.argv[2]; j++) {
    console.log(t);
  }
}
