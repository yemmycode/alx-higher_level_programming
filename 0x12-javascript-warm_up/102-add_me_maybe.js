#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  var incrementedNumber = number + 1;
  theFunction(incrementedNumber);
};
