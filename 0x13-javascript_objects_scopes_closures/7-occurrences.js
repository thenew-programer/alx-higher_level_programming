#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  list.array.forEach((element) => element === searchElement ? occurences++ : '');
  return occurences;
};
