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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
    for (let i = 1; i <= this.heigth; i++) {
      const word = 'X'.repeat(this.width);
      console.log(word);
    }
  }

  double () {
    for (let i = 1; i <= (this.height * 2); i++) {
      const word = 'X'.repeat(this.width * 2);
      console.log(word);
    }
  }
}

module.exports = Rectangle;
