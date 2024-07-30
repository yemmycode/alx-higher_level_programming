#!/usr/bin/node
const x = parseInt(process.argv[2], 10);
if (!Number.isInteger(x)) {
  console.log('Missing number of occurrences');
} else {
  Array.from({ length: x }).forEach(() => console.log('C is fun'));
}
