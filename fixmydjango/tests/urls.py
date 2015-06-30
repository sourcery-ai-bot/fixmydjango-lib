import json

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, View
from django.http import HttpResponse

from .conftest import TEST_JSON_RESPONSE


class SearchTestAPIView(View):

    def get(self, request):
        return HttpResponse(
            json.dumps(TEST_JSON_RESPONSE),
            content_type='application/json')


urlpatterns = patterns('',
    url(r'^error/$', TemplateView.as_view(template_name='none.html'), name='test-error'),
    url(r'^api/search/$', SearchTestAPIView.as_view(), name='test-api'),
)
