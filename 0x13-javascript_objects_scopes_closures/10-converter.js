#!/usr/bin/node

function converter(base) {
    return function(num) {
        return num.toString(base);
    };
}

exports.converter = converter;

