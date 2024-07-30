#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const films = 'https://swapi-api.alx-tools.com/api/films/' + id;
console.log(films);

request(films, (error, response, body) => {
  if (!error) {
    const character = JSON.parse(body).characters;
    character.forEach((charUrl) => {
      request(charUrl, (error, response, body) => {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
