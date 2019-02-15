let elasticsearch = require('elasticsearch');
let RssParser = require('rss-parser');
let sources = require('./sources');

let rss = new RssParser();

let es = new elasticsearch.Client({
    host: 'localhost:9200',
    // log: 'trace'
});


function defaultItemToDoc(item) {
    return {
        title: item.title,
        link: item.link,
        body: item.contentSnippet,
        body_html: item.content,
        pubDate: new Date(item.pubDate),
    }
}

async function sendToElastic(doc) {
    return es.create({
        index: 'rss',
        type: 'item',
        id: doc.link,
        body: doc
    }).catch(err => {
        // if(err.status === 409) {
        //     console.log("already created");
        // }
    });
}

async function handleRss(source) {
    let feed = await rss.parseURL(source.url);

    return Promise.all(feed.items.map(async item => {
        if (source.debug) {
            console.log(item);
            return;
        }

        let itemToDoc = source.itemToDoc || defaultItemToDoc;
        let doc = itemToDoc(item);
        doc.source = source.name;
        doc.category = source.category;

        return await sendToElastic(doc);
    }))
}

async function handleItems(items) {
    return Promise.all(items.map(async item => {
        return await sendToElastic(item);
    }));
}

async function main() {
    Promise.all(sources.map(async source => {
        console.log(source.url);
        if (source.protocol === 'rss' || !source.protocol) {
            return await handleRss(source);
        }
        else if (source.protocol === 'special') {
            let items = await source.handleSpecial(source);
            return await handleItems(items);
        }
    }));
}

main();
