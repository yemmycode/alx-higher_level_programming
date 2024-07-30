#!/usr/bin/node

const calculateFactorial = (num) => {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return num * calculateFactorial(num - 1);
  }
};

const input = Number(process.argv[2]);
console.log(calculateFactorial(input));
