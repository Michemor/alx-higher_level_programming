#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const newText = process.argv[3];
fs.writeFile(filename, newText, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
