#!/usr/bin/node
if (process.argv.length <= 2 || isNaN(parseInt(process.argv[2]))) { console.log('Missing number of occurences'); } else {
  const times = parseInt(process.argv[2]);
  for (let i = 0; i < times; i++) { console.log('C is fun'); }
}
