import fs from 'fs'


// The path is relative to the place from where node is run
let file_contents = fs.readFileSync('package.json')

console.log(file_contents)