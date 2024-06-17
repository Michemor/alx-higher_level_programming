#!/usr/bin/node

const { argv } = require('process');

const toNumber = parseInt(argv[2]);

if (toNumber) {
  for (let i = 0; i < toNumber; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
