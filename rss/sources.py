import json
import os

filepath = os.path.abspath('./node/sources.json')

with open(filepath, 'r') as f:
    sources = json.load(f)


