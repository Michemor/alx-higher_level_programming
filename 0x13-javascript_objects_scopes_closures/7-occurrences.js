#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const n = list.filter((count) => count === searchElement).length;
  return (n);
};
