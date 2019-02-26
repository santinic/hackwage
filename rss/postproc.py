def pre_postproc(doc):
    doc['body_html'] = '<pre>' + doc['body_html'] + '</pre>'


def pre_body_postproc(doc):
    doc['body_html'] = '<pre>' + doc['body'] + '</pre>'


postproc_dict = {
    'GitHub Remote': pre_postproc,
    'RemoteOk': pre_postproc,
    'Coroflot': pre_body_postproc
}


def postproc(doc):
    if doc.source in postproc_dict:
        postproc_dict[doc.source](doc)
    # else:
    #     default_postproc(doc)
