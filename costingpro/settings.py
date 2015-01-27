"""
Django settings for costingpro project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '57*38*e_4w@wj)c3zcip_-at!itgisg&go&$1ag_ywc28o67*l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
SITE_ID = 1

#REGISTRATION_AUTO_LOGIN = True
# REGISTRATION_OPEN = True
# LOGIN_REDIRECT_URL = '/'
# LOGIN_URL = '/accounts/login/'
#ACCOUNT_ACTIVATION_DAYS = 7


# leave uncommented when in production
# =====================================
# EMAIL_HOST = ""
# MAIL_PORT = ""
# etc.


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (

'django.contrib.auth.context_processors.auth',
'django.core.context_processors.csrf',



    )



TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'costingpro', 'templates')),
)

# import pdb; pdb.set_trace()

ROOT_URLCONF = 'costingpro.urls'

WSGI_APPLICATION = 'costingpro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'costingpro',
#         'USER': 'postgres',
#         'HOST': '127.0.0.1',
#         'PORT': '5432'

#     }
# }

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'costingpro.db'),
    }
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',    
    ]


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Kampala'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


# WORK around to check for localsettings file (for development)
# Keep all production settings up... and overrided them in the
# `localsetitings.py` file... an example has been provided.

LOGIN_URL = 'django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = '/business_profile'

try:
    import sys
    if os.environ.has_key('LOCAL_SETTINGS'):
        # the LOCAL_SETTINGS environment variable is used by the build server
        sys.path.insert(0, os.path.dirname(os.environ['LOCAL_SETTINGS']))
        from settings_test import *
    else:
        from localsettings import *
except ImportError:
    pass
