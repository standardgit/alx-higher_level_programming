#!/usr/bin/node

const process = require('process');
const argv = process.argv;

const word = 'C is fun';

for (let i = 0; i < Number(argv[2]); i++) {
  console.log(word);
}
