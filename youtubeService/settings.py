import os
from configparser import RawConfigParser

# NOTICE : you have to change "website_name" to make heroku allow your app as a host


logging_type = "cmd" # it can be "cmd" or "file"
website_name = "YOUR_WEBSITE_NAME"
useGoogleAnalytics = False
googleAnalyticsID = "UA-138713913-1"
DEBUG = False
application_type = "local" # can be "local" or "release"
database_status = "default" # it can be "local" or "global" or "default"


if application_type is "local":
    DEBUG = True
    config = RawConfigParser()
    config.read('youtubeService/settings.ini')

    dataBaseConfigs={
        'ENGINE': config.get('dataBase', 'ENGINE'),
        'NAME': config.get('dataBase', 'NAME'),
        'USER': config.get('dataBase', 'USER'),
        'PASSWORD': config.get('dataBase', 'PASSWORD'),
        'HOST': config.get('dataBase', 'HOST'),
        'PORT': config.get('dataBase', 'PORT'),
    }
    SECRET_KEY = config.get('website', 'SECRET_KEY')
    EMAIL_HOST = config.get('email', 'EMAIL_HOST')
    EMAIL_PORT = config.get('email', 'EMAIL_PORT')
    EMAIL_HOST_USER = config.get('email', 'EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config.get('email', 'EMAIL_HOST_PASSWORD')



elif application_type is "global":
    DEBUG = False
    logging_type = "cmd"


elif application_type is "default":
    DEBUG = False
    config = RawConfigParser()
    config.read('youtubeService/settings.ini')

    SECRET_KEY = config.get('website', 'SECRET_KEY')

    EMAIL_HOST = config.get('email', 'EMAIL_HOST')
    EMAIL_PORT = config.get('email', 'EMAIL_PORT')
    EMAIL_HOST_USER = config.get('email', 'EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config.get('email', 'EMAIL_HOST_PASSWORD')





# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = [
    'localhost',
    "127.0.0.1",
     "0.0.0.0",
     "{}.herokuapp.com".format(website_name),
     "herokuapp.com",
     "https://{}.herokuapp.com/".format(website_name),
     "https://herokuapp.com/",
     ".herokuapp.com"
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "page404.apps.Page404Config",
    "logAuthentication.apps.LogauthenticationConfig",
    "main.apps.MainConfig",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'youtubeService.urls'

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
                "youtubeService.templatesGlobalSettings.adminCustomeSettingsForTemplates",
            ],
        },
    },
]

WSGI_APPLICATION = 'youtubeService.wsgi.application'

if database_status is "local":
    DATABASES = {
        'default': dataBaseConfigs
    }

elif database_status is "global":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '',#database
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }

else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if logging_type is "file":
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt' : "%d/%b/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'mysite.log',
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'django': {
                'handlers':['file'],
                'propagate': True,
                'level':'DEBUG',
            },
            'MYAPP': {
                'handlers': ['file'],
                'level': 'DEBUG',
            },
        }
    }
elif logging_type is "cmd":
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'NOTSET',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': 'NOTSET',
            },
            'django.request': {
                'handlers': ['console'],
                'propagate': False,
                'level': 'ERROR'
            }
        }
    }
else:
    pass

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(STATIC_ROOT, 'static'),
)


EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
