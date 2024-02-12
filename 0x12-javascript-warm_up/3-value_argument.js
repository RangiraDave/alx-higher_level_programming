#!/usr/bin/node
// Script to print first argument

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
