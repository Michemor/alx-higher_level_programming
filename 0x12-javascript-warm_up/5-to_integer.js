#!/usr/bin/node

const { argv } = require('process');
const toNumber = parseInt(argv[2]);

if (toNumber) {
  console.log('My Number: ' + toNumber);
} else {
  console.log('Not a Number');
}
