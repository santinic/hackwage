let fs = require('fs');
let specialSources = require('./special-sources');

let sources = JSON.parse(fs.readFileSync('./sources.json'));

sources.forEach(source => {
    if (specialSources[source.name]) {
        source.handleSpecial = specialSources[source.name];
    }
});

// console.log(sources)

module.exports = sources;