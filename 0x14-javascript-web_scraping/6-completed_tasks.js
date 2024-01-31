#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  try {
    const tasks = JSON.parse(body);
    const completedTasksByUser = countCompletedTasksByUser(tasks);
    console.log(completedTasksByUser);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});

function countCompletedTasksByUser (tasks) {
  const completedTasksCount = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (!completedTasksCount[task.userId]) {
        completedTasksCount[task.userId] = 0;
      }
      completedTasksCount[task.userId]++;
    }
  });

  return completedTasksCount;
}
