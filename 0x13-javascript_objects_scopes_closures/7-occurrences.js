#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((occurences, element) => element === searchElement ? occurences + 1 : occurences, 0);
};
