#!/usr/bin/node
// Writes to a file.

const arg = process.argv;
const fs = require('fs');
const file = arg[2];
const text = arg[3];
fs.writeFile(file, text, 'utf-8', (err) => {
  if (err) throw err;
});
