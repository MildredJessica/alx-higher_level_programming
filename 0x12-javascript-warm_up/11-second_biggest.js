#!/usr/local/bin/node
function maxi (myArray) {
  if (myArray.length === 2 || myArray.length === 3) return 0;
  let max = myArray[2];
  let maxS = myArray[3];
  for (let i = 2; i < myArray.length; i++) {
    if (myArray[i] > max) {
      maxS = max;
      max = myArray[i];
    } else if (myArray[i] > maxS && myArray[i] < max) {
      maxS = myArray[i];
    }
  }
  return maxS;
}
console.log(maxi(process.argv));
