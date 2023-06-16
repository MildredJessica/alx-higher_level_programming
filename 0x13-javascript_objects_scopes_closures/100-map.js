#!/usr/bin/node
const lisarrt = require('./100-data.js').list;
console.log(lisarrt);
let count = 0;
const newList = lisarrt.map(x => x * count++);
console.log(newList);
