#!/usr/bin/node

const filepath = process.argv[2];
const data = process.argv[3];
const fs = require('fs');

try {
    fs.writeFileSync(filepath, data, 'utf8');
    
} catch (error) {
    console.error(error);
}
