#!/usr/bin/node
const Square = require('./5-square');

class square extends Square {
  constructor(size, size) {
    super(size)
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X'
    }
    for (let i = 1; i <= this.height; i++) {                                                         
      const word = 'X'.repeat(this.width);
      console.log(word);                                                                             
    }    	
  }
}
