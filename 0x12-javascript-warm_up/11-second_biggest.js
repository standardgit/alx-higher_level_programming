#!/usr/bin/node

const process = require('process');
const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  console.log(argv.sort((a, b) => b - a)[3]);
}
