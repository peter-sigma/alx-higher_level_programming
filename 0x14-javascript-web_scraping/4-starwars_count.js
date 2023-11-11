#!/usr/bin/node

const myrequest = require('request');
myrequest(process.argv[2], function (error, response, body) {
  if (!error) {
    const myresults = JSON.parse(body).results;

    console.log(myresults.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
