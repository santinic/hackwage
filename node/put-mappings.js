let elasticsearch = require('elasticsearch');
let fs = require('fs');

let es = new elasticsearch.Client({
    host: 'localhost:9200',
    log: 'trace'
});


let body = JSON.parse(fs.readFileSync('./mappings.json'));

let params = {
    index: 'rss',
    type: 'item',
    body: body
};

es.indices.putMapping(params, (err, resp, status) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(resp, status);
});
