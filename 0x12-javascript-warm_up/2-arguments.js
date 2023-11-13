#!/usr/bin/node
const { argv } = require('node:process');

const realArgv = argv.length - 2;
if (realArgv === 0) {
	console.log('No argument');
} else if (realArgv === 1) {
	console.log('Argument found');
}else {
	console.log('Arguments found');
}

