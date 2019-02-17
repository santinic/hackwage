def github_remote_postproc(doc):
    doc['body_html'] = '<pre>'+doc['body']+'</pre>'

postproc = {
    'GitHub Remote': github_remote_postproc
}
