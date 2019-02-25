let elasticsearch = require('elasticsearch');
let RssParser = require('rss-parser');
let sources = require('./sources');
let preproc = require('./preproc');
let httpreq = require('./httpreq');

let rss = new RssParser();

let es = new elasticsearch.Client({
    host: 'localhost:9200',
    // log: 'trace'
});


function defaultItemToDoc(item) {
    return {
        title: item.title.trim(),
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
        if(err.status === 409) {
            // console.log("already created");
        }
        else {
            console.error(err);
        }
    });
}

async function handleRss(source) {
    let xml = await httpreq(source.url).catch(err => {
        console.log(`Cannot fetch ${source.name} ${source.url}`);
        console.error(err);
    });
    let feed = await rss.parseString(xml).catch(err => {
        console.log(`Cannot parse RSS ${source.name} ${source.url}`);
    });

    return Promise.all(feed.items.map(async item => {
        if (source.debug) {
            console.log(item);
            return;
        }

        let itemToDoc = source.itemToDoc || defaultItemToDoc;
        let doc = itemToDoc(item);
        doc.source = source.name;
        doc.category = source.category;
        if (preproc.hasOwnProperty(source.name)) {
            preproc[source.name](doc);
        }

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
            await handleRss(source);
        }
        else if (source.protocol === 'special') {
            let items = await source.handleSpecial(source);
            await handleItems(items);
        }
    }));
}

main();
