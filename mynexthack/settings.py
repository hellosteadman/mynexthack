from os import path, environ

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ['DATABASE_NAME'],
        'USER': environ['DATABASE_USER'],
        'PASSWORD': environ['DATABASE_PASSWORD'],
        'HOST': environ.get('DATABASE_HOST', ''),
        'PORT': environ.get('DATABASE_PORT', '')
    }
}

DEBUG = environ.get('DEBUG') in ('True', 'true', True, 1)
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
OEMBED_DEBUG = DEBUG
ALLOWED_HOSTS = ('*',)

ADMINS = (
	('Steadman', 'mark@steadman.io'),
)

MANAGERS = ADMINS
TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ROOT = path.abspath(path.dirname(__file__) + '/../')
BOWER_COMPONENTS_ROOT = path.join(SITE_ROOT, 'components/')
TEMP_DIR = path.join(SITE_ROOT, 'temp')
STATIC_URL = '/static/'
MEDIA_URL = DEBUG and '/media/' or ('http://%s/media/' % environ.get('DOMAIN', 'mynexthack.com'))
STATIC_ROOT = environ['STATIC_ROOT']
MEDIA_ROOT = environ['MEDIA_ROOT']

STATICFILES_DIRS = (
	# Put strings here, like '/home/html/static' or 'C:/www/django/static'.
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'djangobower.finders.BowerFinder'
)

SECRET_KEY = environ['SECRET_KEY']

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
	'bambu_bootstrap.context_processors.basics',
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
	'django.contrib.humanize',
	'raven.contrib.django.raven_compat',
	'south',
	'taggit',
	'social_auth',
	'bambu_bootstrap',
    'bambu_mail',
    'bambu_markup',
    'mynexthack.core',
	'mynexthack.inspiration',
	'mynexthack.comments'
)

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'social_auth.backends.twitter.TwitterBackend',
	'social_auth.backends.contrib.github.GithubBackend'
)

TWITTER_CONSUMER_KEY = environ['TWITTER_KEY']
TWITTER_CONSUMER_SECRET = environ['TWITTER_SECRET']

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
