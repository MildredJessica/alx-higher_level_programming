#!/usr/bin/node
// Display the status code of a GET request.

const request = require('request');
// const arg = process.argv;
const link = process.argv[2];
request(link, (error, response) => {
  if (error) {
    console.log('error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
