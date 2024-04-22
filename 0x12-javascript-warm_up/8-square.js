#!/usr/bin/node
if (process.argv.length <= 2 || isNaN(parseInt(process.argv[2]))) { console.log('Missing size'); } else {
  const times = parseInt(process.argv[2]);
  for (let i = 0; i < times; i++) {
    console.log('X'.repeat(times));
  }
}
