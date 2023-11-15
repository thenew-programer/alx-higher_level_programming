#!/usr/bin/node
exports.nbOccurences = (list, searchElement) => {
  let occurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      occurrences++;
    }
  }
  return (occurrences);
};
