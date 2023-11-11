#!/usr/bin/node
const s_size = Math.floor(Number(process.argv[2]));
if (isNaN(s_size)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < s_size; r++) {
    let row = '';
    for (let j = 0; j < s_size; j++) row += 'X';
    console.log(row);
  }
}
