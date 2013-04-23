from pinry.settings import *

import os
import sys
import urlparse

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT = os.path.abspath(os.path.dirname(__file__))

# TODO: I recommend using psycopg2 w/ postgres but sqlite3 is good enough.
STACKATO = 'VCAP_APPLICATION' in os.environ

DATABASES = {}
if 'DATABASE_URL' in os.environ:
    url = urlparse.urlparse(os.environ['DATABASE_URL'])
    DATABASES['default'] = {
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
        }
    CACHES = {
        'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': os.getenv('MEMCACHE_URL'),
        }
    }
    if url.scheme == 'postgres':
        DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    elif url.scheme == 'mysql':
        DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or $
        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }


# TODO: Be sure to set this.
SECRET_KEY = 'space-cat'
