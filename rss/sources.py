import json
import os

filepath = os.path.abspath('./node/sources.json')

with open(filepath, 'r') as f:
    sources = json.load(f)


def sources_has_url(url):
    for source in sources:
        if source['url'] == url:
            return True
