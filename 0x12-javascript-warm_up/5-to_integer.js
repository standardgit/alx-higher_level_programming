#!/usr/bin/node

const process = require('process');
const argv = process.argv;

if (argv[2] <= 0 || argv[2] >= 0) {
  console.log(`My number: ${parseInt(argv[2])}`);
} else {
  console.log('Not a number');
}
