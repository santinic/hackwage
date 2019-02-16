from django import forms
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, TemplateView
from elasticsearch_dsl import Search
from django.views.decorators.cache import cache_page
from elasticsearch_dsl.connections import connections

from rss.models import Feedback
from rss.sources import sources

connections.create_connection()
print(connections.get_connection().cluster.health())


def fetch_latest_for_source(source):
    query_body = {
        "size": 20,
        "sort": [
            {"pubDate": {
                "unmapped_type": "date",
                "order": "desc"
            }}
        ],
        "query": {
            "match": {
                "source": source
            }
        }
    }
    query = Search(index='rss', doc_type='item')
    query.update_from_dict(query_body)
    res = query.execute()
    print(source, len(res))
    return res


# @cache_page(60 * 60)
def index(request):
    context = {
        'sources': []
    }
    for source in sources:
        context['sources'].append({
            'desc': source,
            'items': fetch_latest_for_source(source['name'])
        })
    return render(request, 'rss/index.html', context)


def search(request):
    q = request.GET.get('q', '')
    # res = es.search(index='rss', doc_type='item', body={'query': {'query_string': { 'query': q }}})
    query = Search(index='rss').query('query_string', query=q)
    res = query.execute()
    context = {'query': q, 'hits': res.hits}
    return render(request, 'rss/search.html', context)


def item(request):
    id = request.GET.get('id', None)
    if id is None:
        raise Http404('id param not provided.')
    query = Search(index='rss', doc_type='item').query('match', _id=id)
    res = query.execute()
    if len(res.hits) == 0:
        raise Http404("ID does not exists")
    context = {'hit': res.hits[0]}
    return render(request, 'rss/item.html', context)


class FeedbackCreate(CreateView):
    model = Feedback
    fields = ['sender_email', 'message']

    def get_form(self):
        form = super(FeedbackCreate, self).get_form()
        form.fields['message'].widget = forms.Textarea(attrs={'rows':10, 'cols':60})
        return form


feedback_create = FeedbackCreate.as_view(success_url='/feedback/thanks')
feedback_thanks = TemplateView.as_view(template_name='rss/feedback_thanks.html')
# consulting = TemplateView.as_view(template_name='rss/consulting.html')
