#!/usr/bin/node
if (process.argv.length <= 3) {
    console.log(0);
}
else {
    //You might first decide to slice the array first
    console.log(process.argv.sort((a, b) => b - a)[3]);
}
