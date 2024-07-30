#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const userDict = {};
    todos.forEach((task) => {
      if (!userDict[task.userId]) {
        userDict[task.userId] = 0;
      }
      if (task.completed) {
        userDict[task.userId] += 1;
      }
    });
    console.log(userDict);
  }
});
