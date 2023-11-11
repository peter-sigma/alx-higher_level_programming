#!/usr/bin/node

const myreq = require('request');
const myurl = 'https://swapi-api.hbtn.io/api/films/';
const myid = process.argv[2];

myreq.get(myurl + myid, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
