#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request.get(url, (error, response, body) => {
  const movies = JSON.parse(body).title;
  if (error) {
    console.log(error);
  } else {
    console.log(movies);
  }
});
