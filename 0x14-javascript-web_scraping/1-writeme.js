#!/usr/bin/node
const fs = require('fs');

const args = process.argv.slice(2);
const file = args[0];
const str = args[1];

fs.writeFile(file, str, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  console.log(data);
});
