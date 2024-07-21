const fs = require('fs');

const args = process.argv.slice(2);
const file = args[0);

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  console.log('File contents:', data);
});

