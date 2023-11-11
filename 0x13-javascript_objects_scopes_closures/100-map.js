#!/usr/bin/node
const mylist = require('./100-data.js').list;
console.log(mylist);
console.log(mylist.map((item, index) => item * index));
