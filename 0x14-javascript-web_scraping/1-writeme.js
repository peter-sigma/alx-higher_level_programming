#!/usr/bin/node

const myfs = require('fs');
const myfile = process.argv[2];
const mycontent = process.argv[3];

myfs.writeFile(myfile, mycontent, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
