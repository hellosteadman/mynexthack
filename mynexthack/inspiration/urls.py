from django.conf.urls import patterns, url
from bambu.bootstrap.decorators import body_classes
from mynexthack.inspiration.views import *

urlpatterns = patterns('',
	url(r'^all/$', ideas, name = 'all_ideas'),
	url(r'^me/$', my_ideas, name = 'my_ideas'),
	url(r'^(?P<username>[\w]+)/$', body_classes(ideas, 'ideas'), name = 'ideas'),
	url(r'^(?P<username>[\w]+)/(?P<slug>[\w-]{10})/$', body_classes(idea, 'ideas', 'ideas-single'), name = 'idea'),
	url(r'^(?P<username>[\w]+)/(?P<slug>[\w-]{10})/up/', vote, {'value': -1}, name = 'vote_up'),
	url(r'^(?P<username>[\w]+)/(?P<slug>[\w-]{10})/down/', vote, {'value': 1}, name = 'vote_down'),
	url(r'^(?P<username>[\w]+)/(?P<slug>[\w-]{10})/use/', use, name = 'use')
)