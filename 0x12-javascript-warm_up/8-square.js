#!/usr/bin/node
const size = parseInt(process.argv[2], 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  const row = 'X'.repeat(size);
  for (let r = 0; r < size; r++) {
    console.log(row);
  }
}
