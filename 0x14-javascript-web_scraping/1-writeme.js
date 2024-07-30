#!/usr/bin/node

const fs = require('fs');
const [filename, content] = process.argv.slice(2);

fs.writeFile(filename, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
