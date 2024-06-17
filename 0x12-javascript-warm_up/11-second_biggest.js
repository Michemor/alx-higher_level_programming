#!/usr/bin/node

const { argv } = require('process');
let largest = 0;
let secondLargest = 0;

if (argv.length > 3) {
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i], 10);

    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }
}
console.log(secondLargest);
