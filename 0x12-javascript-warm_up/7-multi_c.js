#!/usr/bin/node

const argv1 = process.argv[2];
const x = argv1;

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
