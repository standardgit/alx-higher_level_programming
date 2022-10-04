#!/usr/bin/node

const process = require('process');
const argv = process.argv;

function factorial (num) {
  if (num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

if (argv[2] <= 0 || argv[2] >= 0) {
  console.log(factorial(Number(argv[2])));
} else {
  console.log(1);
}
