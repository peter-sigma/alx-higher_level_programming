#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
const n1 = process.argv[2];
const n2 = process.argv[3];
console.log(add(n1, n2));
