#!/usr/bin/node

const myrequest = require('request');
const myurl = process.argv[2];

myrequest(myurl, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
