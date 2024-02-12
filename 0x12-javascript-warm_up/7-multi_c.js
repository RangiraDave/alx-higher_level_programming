#!/usr/bin/node
// printing message multiple times acording to the first argv

if (!Number(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i < Number(process.argv[2]) + 1; i++) {
    console.log('C is fun');
  }
}
