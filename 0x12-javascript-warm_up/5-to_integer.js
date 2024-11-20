#!/usr/bin/node
if (Object.is(parseInt(process.argv[2]), NaN)) {
    console.log("Not a number");
}
else {
    console.log(parseInt(process.argv[2]));
}
