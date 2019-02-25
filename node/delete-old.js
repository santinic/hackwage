let elasticsearch = require('elasticsearch');

let es = new elasticsearch.Client({
    host: 'localhost:9200',
    log: 'trace'
});


es.deleteByQuery({
    index: 'rss',
});
