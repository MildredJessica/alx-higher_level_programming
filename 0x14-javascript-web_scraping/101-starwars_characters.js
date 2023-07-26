#!/usr/bin/node
// Print Star Wars characters in order of URL listing.

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, pos) {
  request(characters[pos], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (pos + 1 < characters.length) {
        printCharacters(characters, pos + 1);
      }
    }
  });
}
