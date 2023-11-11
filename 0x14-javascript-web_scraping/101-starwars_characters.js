#!/usr/bin/node

const myrequest = require('request');
const myurl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

myrequest(myurl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printChars(characters, 0);
  }
});

function printChars (characters, index) {
  myrequest(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);

      if (index + 1 < characters.length) {
        printChars(characters, index + 1);
      }
    }
  });
}
