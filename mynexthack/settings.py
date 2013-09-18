from settings_local import *
from os import path

TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Mark Steadman', 'marksteadman@me.com'),
)

MANAGERS = ADMINS
TIME_ZONE = None
LANGUAGE_CODE = 'en-gb'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ROOT = path.abspath(path.dirname(__file__) + '/../')
MEDIA_ROOT = path.join(SITE_ROOT, 'media') + '/'
STATIC_ROOT = path.join(SITE_ROOT, 'static') + '/'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
	# Put strings here, like '/home/html/static' or 'C:/www/django/static'.
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '2lb&amp;d95d+dd)jz(8ru3=9o((b1av)lf^@t^mp!b40g0anyh&amp;&amp;7'

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader'
)

MIDDLEWARE_CLASSES = (
	'django.middleware.cache.UpdateCacheMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.cache.FetchFromCacheMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
	'django.core.context_processors.tz',
	'social_auth.context_processors.social_auth_by_name_backends',
	'social_auth.context_processors.social_auth_backends',
	'social_auth.context_processors.social_auth_by_type_backends',
	'social_auth.context_processors.social_auth_login_redirect',
	'bambu.bootstrap.context_processors.basics',
	'mynexthack.inspiration.context_processors.ideas'
)

ROOT_URLCONF = 'mynexthack.urls'

TEMPLATE_DIRS = (
	path.join(SITE_ROOT, 'templates') + '/',
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'django.contrib.admindocs',
	'django.contrib.markup',
	'django.contrib.humanize',
	'raven.contrib.django.raven_compat',
	'south',
	'taggit',
	'social_auth',
	'bambu.bootstrap',
	'bambu.pages',
	'bambu.faq',
	'bambu.fileupload',
	'bambu.jwplayer',
	'bambu.attachments',
	'bambu.enquiries',
	'bambu.enqueue',
	'bambu.mail',
	'bambu.grids',
	'mynexthack.inspiration',
	'mynexthack.comments'
)

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'social_auth.backends.twitter.TwitterBackend',
	'social_auth.backends.contrib.github.GithubBackend'
)

TWITTER_CONSUMER_KEY = 'Z9pd6izLv3d73JkfCuafKQ'
TWITTER_CONSUMER_SECRET = 'xA31LNupVUY6hcYR0iYL4vKvWX3nVwvxk4wId9BSY'

LOGIN_URL = '/login/twitter/'
LOGIN_REDIRECT_URL = '/me/'
ATOMIC_REQUESTS = True

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}

BOOTSTRAP_NAVBAR_INVERSE = True
TYPEKIT_KEY = 'vid0zdl'