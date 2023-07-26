#!/usr/bin/node
// Prints the number of movies where
// the character “Wedge Antilles” is present

const req = require('request');
const url = process.argv[2];
const charID = '18';
req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const respBody = JSON.parse(body);
    let count = 0;
    for (const i of respBody.results) {
      for (const j of i.characters) {
        if (j.search(charID) > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
