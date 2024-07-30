#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log('Error');
  } else {
    const result = JSON.parse(body).results;
    const count = result.reduce((count, movie) => {
      const end18 = movie.characters.find((c) => c.endsWith('/18/'));
      return end18 ? count + 1 : count;
    }, 0);
    console.log(count);
  }
});
