from pinry.settings import *

import os


DEBUG = False
TEMPLATE_DEBUG = DEBUG

# TODO: I recommend using psycopg2 w/ postgres but sqlite3 is good enough.
import urlparse
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
    if url.scheme == 'postgres':
        DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    elif url.scheme == 'mysql':
        DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }


# TODO: Be sure to set this.
SECRET_KEY = 'blarg2+@tr!=36rrh(vn@b*1ya=m1jti=0&8zn68@=@)y11==9%wf7v'
