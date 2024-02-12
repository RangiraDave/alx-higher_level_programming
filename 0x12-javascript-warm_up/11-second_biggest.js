#!/usr/bin/node
// Script to search for second large number in a list of args.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let max = Number.MIN_SAFE_INTEGER;
  let sec = Number.MIN_SAFE_INTEGER;
  process.argv.forEach((val, index) => {
    if (index > 1) {
      const n = parseInt(val);
      if (n > max) {
        sec = max;
        max = n;
      } else if (n > sec && n < max) {
        sec = n;
      }
    }
  });
  console.log(sec);
}
