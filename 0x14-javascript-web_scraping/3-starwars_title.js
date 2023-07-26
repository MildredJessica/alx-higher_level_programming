#!/usr/bin/node
// Prints the title of a Star Wars movie
// where the episode number matches a given integer.

const req = require('request');
const filmID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmID;
req(url, (error, response, body) => {
  if (error === null) {
    const responseBody = JSON.parse(body);
    console.log(responseBody.title);
  } else {
    console.log(error);
  }
});
