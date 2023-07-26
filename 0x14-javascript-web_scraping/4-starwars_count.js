#!/usr/bin/node
// Prints the number of movies where
// the character “Wedge Antilles” is present

const req = require('request');
const url = process.argv[2];
const charID = '18/';
req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const respBody = JSON.parse(body).results;
    let count = 0;
    for (let k = 0; k < respBody.length; k++) {
      const characters = respBody[k].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].endsWith(charID)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
