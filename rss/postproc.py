from rss.templates.rss.linkurls import linkurls


def pre_postproc(doc):
    doc['body_html'] = '<pre>' + doc['body_html'] + '</pre>'


# def default_postproc(doc):
#     doc['body_html'] = linkurls(doc['body_html'])


postproc_dict = {
    'GitHub Remote': pre_postproc,
    'RemoteOk': pre_postproc,
}


def postproc(doc):
    if doc.source in postproc_dict:
        postproc_dict[doc.source](doc)
    # else:
    #     default_postproc(doc)
