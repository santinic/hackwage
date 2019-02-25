import json
import os
from urllib.parse import urlparse


filepath = os.path.abspath('./node/sources.json')

with open(filepath, 'r') as f:
    sources = json.load(f)


def sources_has_url(url):
    for source in sources:
        if source['url'] == url:
            return True


def sources_has_netloc(netloc):
    for source in sources:
        parsed = urlparse(source['url'])
        if parsed.netloc == netloc:
            return True
    return False
