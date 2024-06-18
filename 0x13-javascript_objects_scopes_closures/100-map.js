#!/usr/bin/node

const list = require('./100-data.js').list;
const newList = list.map((n, i) => n * i);
console.log(list);
console.log(newList);
