#!/usr/bin/node

const myfs = require('fs');
const myrequest = require('request');

myrequest(process.argv[2]).pipe(myfs.createWriteStream(process.argv[3]));
