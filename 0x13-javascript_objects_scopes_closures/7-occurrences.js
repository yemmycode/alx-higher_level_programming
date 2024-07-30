#!/usr/bin/node
module.exports.nbOccurences = function countOccurrences(list, searchElement) {
  return list.reduce(function(count, current) {
    return current === searchElement ? count + 1 : count;
  }, 0);
};
