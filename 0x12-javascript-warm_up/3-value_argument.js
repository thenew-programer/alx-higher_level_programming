#!/usr/bin/node
let i = 0;
for (i = 0; i < 1000; i++) {
  if (i >= 2 && process.argv[i] !== undefined) {
    console.log(process.argv[i]);
  }
}
if (i === 2) console.log('No argument');
