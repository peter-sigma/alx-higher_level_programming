#!/usr/bin/node
const mydict = require('./101-data').dict;

const mytotalist = Object.entries(mydict);
const myvals = Object.values(mydict);
const valUniq = [...new Set(myvals)];
const newDict = {};
for (const j in valUniq) {
	const list = [];
	for (const k in mytotalist) {
		if (mytotalist[k][1] === valUniq[j]) {
			list.unshift(mytotalist[k][0]);
		}
	}
	newDict[valUniq[j]] = list;
}
console.log(newDict);
