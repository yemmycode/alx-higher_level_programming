#!/usr/bin/node
const SquareBase = require('./5-square.js');

module.exports = class Square extends SquareBase {
  charPrint(c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
