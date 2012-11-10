import dj_database_url
import os
from boto.s3.connection import OrdinaryCallingFormat

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

#s3 settings
AWS_ACCESS_KEY_ID = os.environ.get('S3_KEY', None)
AWS_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET', None)
AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET', None)
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()


MEDIA_ROOT = "/"
MEDIA_URL = 'http://s3.amazonaws.com/%s/media' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = '/static/'
STATIC_URL = 'http://s3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME

STATICFILES_DIRS = (
    os.path.join(ROOT_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
#    'pipeline.finders.PipelineFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'v+^uyi8-ttp3gn)m^na+__*sbk&amp;0*dzo6zi3da&amp;05(toxbb^=h'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'heroku_template.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'heroku_template.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOT_DIR, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    ####
    'gunicorn',
    'pipeline',
    'storages',
    ####
    'main',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

#django-pipeline settings
PIPELINE = not DEBUG

PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
          'less/bootstrap/bootstrap.less',
          'less/main.less',
        ),
        'output_filename': 'css/bootstrap.css',
        'extra_context': {
            'rel': 'stylesheet/less',
        },
    },
    'index': {
        'source_filenames': (
          'less/index.less',
        ),
        'output_filename': 'css/index.min.css',
        'extra_context': {
            'rel': 'stylesheet/less',
        },
    },
}

PIPELINE_JS = {
    'core': {
        'source_filenames': (
            'js/jquery-1.7.2.js',
            'js/underscore.js',
            'js/backbone.js',
        ),
        'output_filename': 'js/core.min.js',
    },
    'index': {
        'source_filenames': (
            'js/bootstrap-transition.js',
            'js/bootstrap-carousel.js',
            ),
        'output_filename': 'js/index.min.js',
    }
}

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CssminCompressor'

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)

STATICFILES_STORAGE = 'heroku_template.storage.S3PipelineStorage'
PIPELINE_LESS_BINARY = '/app/bin/node /app/lessc.js'
PIPELINE_COFFEE_SCRIPT_BINARY = '/app/bin/node /app/coffee.js'
PIPELINE_COFFEE_SCRIPT_ARGUMENTS = '-c'

PIPELINE_TEMPLATE_FUNC = 'new EJS'
PIPELINE_TEMPLATE_NAMESPACE = 'window.Template'
PIPELINE_TEMPLATE_EXT = '.ejs'
