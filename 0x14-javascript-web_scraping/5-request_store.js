#!/usr/bin/node
const fs = require('fs');
const request = require('request');
if (process.argv.length !== 4) {
  console.error('Usage: ./4-request_store.js <URL> <file path>');
  process.exit(1);
}
const url = process.argv[2];
const filePath = process.argv[3];
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error('Error:', `Failed to fetch URL. Status code: ${response.statusCode}`);
    process.exit(1);
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error('Error:', err);
      process.exit(1);
    }
    console.log(`Successfully saved the contents of ${url} to ${filePath}`);
  });
});
