#!/usr/local/bin/node
// Computes the number of tasks completed by user id.

const request = require('request');
const arg = process.argv;
const url = arg[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const respBody = JSON.parse(body);
    const todos = {};
    for (let w = 0; w < respBody.length; w++) {
      const key = respBody[w].userId.toString();
      if (respBody[w].completed) {
        if (todos[key]) {
          todos[key]++;
        } else {
          todos[key] = 1;
        }
      }
    }
    console.log(todos);
  }
});
