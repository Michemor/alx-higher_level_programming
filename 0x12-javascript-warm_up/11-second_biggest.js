#!/usr/bin/node

let largest = 0;
let secondLargest = 0;
if (process.argv.length > 3) {
  for (let i = 2; i < process.argv.length; i++) {
    const num = parseInt(process.argv[i], 10);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }
}
console.log(secondLargest);
