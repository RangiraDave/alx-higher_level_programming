#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size);
    if (Number(size) && Number(size) > 0) {
      this.size = size;
    }
  }

  charPrint (c) {
    let temp;
    if (c) {
      temp = c;
    } else {
      temp = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write(temp);
      }
      console.log();
    }
  }
}

module.exports = Square;
