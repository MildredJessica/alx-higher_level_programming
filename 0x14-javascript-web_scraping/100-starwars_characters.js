#!/usr/bin/node
// Prints all characters of a Star Wars movie.

const req = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
req.get(url, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body).characters;
  for (const p of data) {
    req.get(p, function (err, res, body) {
      if (err) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
