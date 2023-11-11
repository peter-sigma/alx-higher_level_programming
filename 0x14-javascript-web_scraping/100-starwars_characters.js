#!/usr/bin/node

const myrequest = require('request');
myrequest(process.argv[2], function (error, response, body) {
  if (!error) {
    const tasks = JSON.parse(body);
    const completed = {};
    tasks.forEach((t) => {
      if (t.completed && completed[t.userId] === undefined) {
        completed[t.userId] = 1;
      } else if (t.completed) {
        completed[t.userId] += 1;
      }
    });

    console.log(completed);
  }
});
