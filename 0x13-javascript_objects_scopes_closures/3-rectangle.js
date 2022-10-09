#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      const word = 'X'.repeat(this.width);
      console.log(word);
    }
  }
}

module.exports = Rectangle;
