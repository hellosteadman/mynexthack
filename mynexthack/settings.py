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
WSGI_APPLICATION = 'mynexthack.wsgi.application'

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
    'djangobower',
	'bambu_bootstrap',
    'bambu_mail',
    'bambu_markup',
    'mynexthack.core',
	'mynexthack.inspiration',
	'mynexthack.comments',
    'raven.contrib.django.raven_compat'
)

BOWER_INSTALLED_APPS = (
    'bootstrap',
    'fontawesome'
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
    'disable_existing_loggers': True,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    },
    'formatters': {
        'verbose': {
            'format': '%(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False
        },
        'south': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False
        },
        'bambu_cron': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        }
    }
}

if not DEBUG:
    LOGGING['handlers']['sentry'] = {
        'level': 'ERROR',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
    }

    LOGGING['loggers']['sentry.errors'] = {
        'level': 'DEBUG',
        'handlers': ['console'],
        'propagate': False
    }

    RAVEN_CONFIG = {
        'dsn': 'http://4d37d8fa60184e3fa522f0a680c7e2fd:0439f8de7aab4a9e9c5027c57fde3c11@blossom.cloud.steadman.io/7',
    }

BOOTSTRAP_NAVBAR_INVERSE = True
TYPEKIT_KEY = 'vid0zdl'
