#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No arguments found');
}
if (process.argv.length > 2) {
  if (process.argv.length === 3) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}
