#!/usr/bin/node

const { argv } = require('process');
const size = parseInt(argv[2]);
if (size) {
  for (let i = 0; i < size; i++) {
    let symbol = '';
    for (let j = 0; j < size; j++) {
      symbol += 'X';
    }
    console.log(symbol);
  }
} else {
  console.log('Missing size');
}
