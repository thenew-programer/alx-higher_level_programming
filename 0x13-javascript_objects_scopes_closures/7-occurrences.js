#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  return list.array.forEach((element) => element === searchElement ? occurences++ : occurences);
};
