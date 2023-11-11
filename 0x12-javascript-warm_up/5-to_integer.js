#!/usr/bin/node

const myNumber = process.argv[2];
const valid = parseInt(myNumber);

if (isNaN(valid)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${valid}`);
}
