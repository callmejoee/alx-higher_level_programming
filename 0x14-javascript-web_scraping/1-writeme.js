#!/usr/bin/node
const fs = require('fs');

const args = process.argv.slice(2);
const file = args[0];
const str = args[1];

fs.writeFile(file, str, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
  }
});
