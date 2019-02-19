let request = require('request');

function httpreq(url) {
    return new Promise(function (resolve, reject) {
        let params = {
            method: "GET",
            url: url,
            rejectUnauthorized: false
        };
        request(params, function (error, res, body) {
            if (!error && res.statusCode === 200) {
                resolve(body);
            } else {
                console.error(error);
                reject(error);
            }
        });
    });
}

module.exports = httpreq;