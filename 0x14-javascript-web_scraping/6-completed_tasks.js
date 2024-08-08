#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get({ url, json: true }, (err, res, data) => {
  if (err) {
    console.log(err);
    return;
  }

  const completedTasks = {};
  data.forEach((todo) => {
    if (todo.completed) {
      completedTasks[todo.userId] = (completedTasks[todo.userId] || 0) + 1;
    }
  });

  console.log(completedTasks);
});
