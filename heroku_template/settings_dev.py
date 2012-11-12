from settings import *

STATIC_ROOT = os.path.join(ROOT_DIR, '..', 'collected_static')
STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, '..', 'database.sqlite3.db'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG = True
PIPELINE = False

PIPELINE_COMPILERS = ()


PIPELINE_JS['core']['source_filenames'] += ('js/less-1.3.0.min.js', 'js/coffee-script.js')
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_LESS_BINARY = '/usr/local/bin/lessc'
PIPELINE_COFFEE_SCRIPT_BINARY = '/usr/local/bin/coffee'
