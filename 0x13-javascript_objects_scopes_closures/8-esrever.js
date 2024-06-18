#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    reverseList[j++] = list[i];
  }
  return reverseList;
};
