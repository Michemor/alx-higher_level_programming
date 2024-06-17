#!/usr/bin/node

const { argv } = require('process');

const to_number = parseInt(argv[2]);

if (to_number) {
  console.log('My Number: ' + to_number);
} else {
  console.log('Not a Number');
}
