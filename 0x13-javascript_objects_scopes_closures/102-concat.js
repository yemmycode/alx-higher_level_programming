#!/usr/bin/node
const fs = require('fs');

const [,, inputFile1, inputFile2, outputFile] = process.argv;

const contentA = fs.readFileSync(inputFile1, 'utf8');
const contentB = fs.readFileSync(inputFile2, 'utf8');

fs.writeFileSync(outputFile, contentA + contentB);
