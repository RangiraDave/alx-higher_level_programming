#!/usr/bin/node
// Script to convert first argument to int

if (Number(process.argv[2])) {
  console.log(`My number: ${Number(process.argv[2]).toFixed()}`);
} else {
  console.log('Not a number');
}
