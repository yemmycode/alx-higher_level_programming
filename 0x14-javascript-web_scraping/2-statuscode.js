#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node <script-file> <URL>');
  process.exit(1);
}

const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error('Request error:', error);
    process.exit(1);
  }

  console.log(`code: ${response.statusCode}`);
});
