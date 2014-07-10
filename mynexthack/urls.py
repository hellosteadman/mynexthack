from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.decorators.vary import vary_on_cookie
from bambu_bootstrap.views import DirectTemplateView
from bambu_bootstrap.decorators import body_classes

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$',
		vary_on_cookie(
			body_classes(
				DirectTemplateView.as_view(template_name = 'home.html'), 'home'
			)
		),
		name = 'home'
	),
	url(r'^mail/', include('bambu_mail.urls')),
	url(r'logout/$',
		'django.contrib.auth.views.logout',
		{
			'next_page': '/'
		},
		name = 'logout'
	),
	url(r'', include('social_auth.urls')),
	url(r'^', include('mynexthack.inspiration.urls'))
)
