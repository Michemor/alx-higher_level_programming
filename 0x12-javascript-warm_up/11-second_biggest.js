#!/usr/bin/node

const { argv } = require('process');
let largest = 0;
let second_largest = 0;

if (argv.length > 3) {
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i], 10);

    if (num > largest) {
      second_largest = largest;
      largest = num;
    } else if (num > second_largest && num !== largest) {
      second_largest = num;
    }
  }
}
console.log(second_largest);
