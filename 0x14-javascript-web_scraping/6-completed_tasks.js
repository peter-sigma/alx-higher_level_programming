#!/usr/bin/node

const myrequest = require('request');

myrequest(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const completed_tasks = {};

    todos.forEach((todo) => {
      if (todo.completed_tasks && completed_tasks[todo.userId] === undefined) {
        completed_tasks[todo.userId] = 1;
      } else if (todo.completed_tasks) {
        completed_tasks[todo.userId] += 1;
      }
    });
    console.log(completed_tasks);
  }
});
