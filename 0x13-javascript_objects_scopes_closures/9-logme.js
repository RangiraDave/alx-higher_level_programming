#!/usr/bin/node
let i = 0;
exports.logMe = function (item) {
//  let i = 0;
  console.log(`${i}: ${item}`);
  i += 1;
  //  console.log(`${i}: ${item}`);
};
