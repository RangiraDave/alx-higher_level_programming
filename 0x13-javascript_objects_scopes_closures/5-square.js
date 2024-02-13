#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size);
    this.size = size;
  }

  print () {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  double () {
    this.size *= 2;
  }
}

module.exports = Square;
