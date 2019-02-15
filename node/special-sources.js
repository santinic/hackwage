const fetch = require("node-fetch");

let specialSources = {
    'Working Nomads': async function (source) {
        let response = await fetch(source.url).catch(err => console.error(err));
        if (response.status !== 200) {
            console.error("Working Nomands error", response);
            return;
        }
        let body = response.json();
        // console.log(body)

        return items.map(item => {
            return {
                pubDate: item.pub_date,
                body_html: item.description,
                title: item.title,
                link: item.url
            };
        });
    }
};

module.exports = specialSources;