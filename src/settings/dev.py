from configurations import Configuration, values

import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Dev(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'w$f#62^kn_)oj_c+m3uvjs8nq^*+&ey7#4%5@47hs)$drnz%k)'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []


    # Application definition

    DJANGO_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        )

    THIRDPARTY_APPS = (
        'markdown',
        'rest_framework',
        'rest_framework.authtoken',
        'rest_auth',
        'django_admin_bootstrapped',
        'corsheaders',
        )

    LOCAL_APPS = (
        'freeradius',
        'radauth',
        )

    INSTALLED_APPS = (
        ) + THIRDPARTY_APPS + DJANGO_APPS  + LOCAL_APPS



    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )

    ROOT_URLCONF = 'radius.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'radius.wsgi.application'

    AUTHENTICATION_BACKENDS = (
        'radiusauth.backends.RADIUSBackend',
        'django.contrib.auth.backends.ModelBackend',
    )

    RADIUS_SERVER = 'radius'
    RADIUS_PORT = 1812
    RADIUS_SECRET = 'password'

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        )
    }


    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        },
        'radius': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'radius',
            'USER': 'radius',
            'PASSWORD': 'radius',
            'HOST': 'mysqldb',
        }
    }

    DATABASE_ROUTERS = ['radius.dbrouter.DBRouter']

    # Internationalization
    # https://docs.djangoproject.com/en/1.8/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'Australia/Sydney'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    CORS_ORIGIN_ALLOW_ALL = True

    DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

    from django.contrib import messages

    MESSAGE_TAGS = {
                messages.SUCCESS: 'alert-success success',
                messages.WARNING: 'alert-warning warning',
                messages.ERROR: 'alert-danger error'
    }

    # Custom User Model
    AUTH_USER_MODEL = 'radauth.RadiusUser'

    #DEFAULT_CONTENT_TYPE = 'application/xhtml+xml'

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/

    STATIC_URL = '/static/'
