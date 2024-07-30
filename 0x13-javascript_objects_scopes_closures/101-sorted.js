#!/usr/bin/node
const { dict: dictInput } = require('./101-data');
const outDict = {};

Object.entries(dictInput).forEach(([key, value]) => {
    if (!outDict[value]) {
        outDict[value] = [];
    }
    outDict[value].push(key);
});

console.log(outDict);
