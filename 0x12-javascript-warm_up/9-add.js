#!/usr/bin/node

const sum = (x, y) => x + y;

const arg1 = parseInt(process.argv[2], 10);
const arg2 = parseInt(process.argv[3], 10);

console.log(sum(arg1, arg2));
