#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = list.filter((count) => count === searchElement).length 
  return (n);
}
