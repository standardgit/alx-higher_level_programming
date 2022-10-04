#!/usr/bin/node

const process = require('process');
const argv = process.argv;

const fact = (num) => {
  if (num === 1) {
    return 1;
  }
  return num * fact(num - 1);
};

if (argv[2] <= 0 || argv[2] >= 0) {
  console.log(fact(Number(argv[2])));
} else {
  console.log(1);
}
