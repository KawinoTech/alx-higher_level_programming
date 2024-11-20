#!/usr/bin/node
if (Object.is(parseInt(process.argv[2]), NaN)) {
  console.log('Missing number of occurrences');
} else if (parseInt(process.argv[2]) <= 0);
else {
  for (let i = 0; i !== process.argv[2]; i++) {
    console.log('C is fun');
  }
}
