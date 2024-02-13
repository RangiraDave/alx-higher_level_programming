#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number(w) && Number(h)) {
      if (Number(w) > 0 && Number(h) > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
