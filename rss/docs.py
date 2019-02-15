from datetime import datetime
from elasticsearch_dsl import DocType, Text, Date, Search


class ItemIndex(DocType):
    title = Text()
    pubDate = Date()
    body = Text()
    body_html = Text()

    class Meta:
        index = 'rss'

# ItemIndex.init()
