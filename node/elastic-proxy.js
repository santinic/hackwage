let express = require('express');
let app = express();
let elasticsearch = require('elasticsearch');

let es = new elasticsearch.Client({
    host: 'localhost:9200',
    log: 'trace'
});

app.get('/search/:q', function (req, res, next) {
    if(!req.params.q) {
        return next("No q param");
    }

    let esParams = {
        index: 'rss',
        q: req.params.q
    };
    es.search(esParams, (err, esRes) => {
        // console.log(err, esRes)
        res.send(esRes);
    });
});

app.listen(3000);