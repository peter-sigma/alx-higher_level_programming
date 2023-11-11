#!/usr/bin/node

const argv1 = process.argv[2];

if (argv1) {
  console.log(argv1);
} else {
  console.log('No argument');
}
