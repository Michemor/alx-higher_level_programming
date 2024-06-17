#!/usr/bin/node
const { argv } = require('process');
const argvlength = argv.length - 2;

if (argvlength <= 0) {
  console.log('No argument');
} else if (argvlength === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
