#!/usr/bin/node
if (process.argv.length <= 3) console.log(0);
else {
  const listlen = process.argv.length - 2;
  const list = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(list[listlen - 2]);
}
