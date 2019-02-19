import csv
import json

import os

filepath = os.path.abspath('../sources.json')

with open(filepath, 'r') as f:
    sources = json.load(f)


def sources_has_url(url):
    for source in sources:
        if source['url'] == url:
            return True


with open('./remote-list.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    urls = sources
    for row in reader:
        url = row['Feed URL']
        if url is None:
            continue

        if not sources_has_url(url):
            urls.append({
                'name': row['Title'],
                'url': url,
                'category': 'jobs'
            })
    print(json.dumps(urls))
