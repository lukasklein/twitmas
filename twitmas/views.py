import requests
import json
from django.views.generic import TemplateView
from django.http import HttpResponse


class TwitmasView(TemplateView):
    template_name = 'index.html'


def get_tweet(request):
    keyword = request.GET.get('keyword')

    search_url = 'http://search.twitter.com/search.json?q=%s'
    r = requests.get(search_url % keyword)
    search_results = json.loads(r.text)['results']

    tweet = search_results[0]['text'].lower()
    tweet_markup = tweet.replace(keyword, '<span class="kw">%s</span>' % keyword, 1)
    author = search_results[0]['from_user'].lower()

    html_template = '%s - %s' % (tweet_markup, author)

    return HttpResponse(html_template)
