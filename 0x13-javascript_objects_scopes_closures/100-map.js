#!/usr/bin/node

const listData = require('./100-data.js');

const list = listData.list;

const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
