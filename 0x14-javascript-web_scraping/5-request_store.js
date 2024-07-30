#!/usr/bin/node

const fs = require('fs');
const request = require('request');

if (process.argv.length < 4) {
  console.error('Usage: node <script-file> <URL> <output-file>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.error('Request error:', err);
    process.exit(1);
  }

  fs.writeFile(filePath, body, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
});
