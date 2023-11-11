#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
    charPrint (c) {
        if (c === undefined) {
    	     c ='X';
	}
	for (let i = 0; i < this.height; i++) {
	    let s = '';
    	    for (let i = 0; i < this.width; i++) {
                s += c;
            }
	    console.log(s);
	}
    }
}

module.exports = Square;
