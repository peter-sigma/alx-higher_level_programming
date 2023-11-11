#!/usr/bin/node
function factorial (number) {
  if (number === 0 || number === 1) {
    return 1;
  } else {
    return factorial(number - 1) * number;
  }
}
const myargs = process.argv[2];
if (myargs === undefined) {
  console.log(1);
} else {
  console.log(factorial(myargs));
}
