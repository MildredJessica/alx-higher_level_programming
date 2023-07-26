#!/usr/bin/node
// Reads and prints the content of a file.

const arg = process.argv;
const fs = require('fs');
const fi = arg[2];
fs.readFile(fi, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data + '\n');
  }
});
