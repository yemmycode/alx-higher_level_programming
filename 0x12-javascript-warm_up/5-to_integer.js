#!/usr/bin/node
const input = process.argv[2];
const parsedNum = parseInt(input, 10);

if (isNaN(parsedNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedNum}`);
}
