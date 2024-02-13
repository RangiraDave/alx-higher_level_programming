#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0 && j < list.length; i--, j++) {
    rev[j] = list[i];
  }
  list = rev;
  return list;
};
