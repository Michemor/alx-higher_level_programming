#!/usr/bin/node

const { argv } = require('process');
const len = argv.length - 2;

if (len <= 0) {
  console.log('No argument');
} else if (len === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
