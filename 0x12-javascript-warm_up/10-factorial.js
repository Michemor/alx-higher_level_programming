#!/usr/bin/node

function fact (n) {
  if (n === 1) {
    return (n);
  } else {
    return (fact(n - 1) * n);
  }
}

const { argv } = require('process');
const val = parseInt(argv[2]);

if (val) {
  console.log(fact(val));
} else {
  console.log(1);
}
