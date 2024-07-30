#!/usr/bin/node
module.exports = {
  esrever: function(list) {
    var reversed = [];
    list.reduceRight(function(array, current) {
      reversed.push(current);
      return array;
    }, []);
    return reversed;
  }
};

