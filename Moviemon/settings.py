"""
Django settings for Moviemon project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v@i%$w*s)vmwa)-wddj+q0^ae9&mt5-i*c9wu3xc+m&beqz4pd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'mainpage.apps.MainpageConfig',
    'moviedex.apps.MoviedexConfig',
    'options.apps.OptionsConfig',
    'worldmap.apps.WorldmapConfig',
    'battle.apps.BattleConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Moviemon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
	    ,
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

WSGI_APPLICATION = 'Moviemon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

OMDB_APIKEY = os.environ.get('OMDB_APIKEY') or '7d9dfd8c'
OMDB_URL = 'http://www.omdbapi.com'

MAP_SIZE = (20, 20)
FRAME_SIZE = (11, 11)
DEFAULT_PLAYER_POSITION = (5, 5)
DEFAULT_PLAYER_STRENGTH = 5
DEFAULT_PLAYER_MOVIEBALLS = 10

MOVIE_IDS = {
    'tt0060666',
    'tt4058836',
    'tt12163074',
    'tt1099212',
    'tt9737326',
    'tt13109952',
    'tt9243804',
    'tt0107688',
    'tt0381061',
    'tt0111161',
    'tt10665338',
    'tt9421570',
    "tt0468492",
    "tt5034838",
    "tt0078748",
    "tt0087363",
    "tt0073195",
    "tt8235660",
    "tt0118615",
    "tt0105643",
    "tt1844770",
    "tt0329101",
    "tt0372873",
    "tt1934381",
    "tt1270797",
    "tt3967856",
    "tt10240612",
    "tt0317676",
    "tt1489946",
    "tt1714203",
    "tt5639976",
    "tt6644200",
    "tt0198781",
    "tt0091064",
    "tt4680182",
    "tt2231461",
    "tt0100814",
    "tt5688868",
    "tt4374286",
    "tt0069005",
    "tt0100260",
    "tt0089469",
    "tt0055894",
    "tt1396484",
    "tt0065163",
    "tt0090190",
    "tt0084745",
    "tt0457430",
    "tt0093177",
    "tt0083907",
    "tt5884052",
    "tt3794354",
    "tt7504864",
    "tt1415872",
    "tt7904362",
    "tt1788453",
    "tt0272425",
    "tt0289181",
    "tt0327169",
    "tt0364569",
    "tt0406661",
    "tt0428870",
    "tt1606283",
    "tt2972482",
    "tt2990738",
    "tt4682562",
    "tt4844288",
    "tt5066556",
    "tt5068856",
    "tt5215952",
    "tt6890582",
    "tt6904062",
    "tt7046826",
    "tt7057496",
    "tt8290698",
    "tt8850222",
    "tt10530286",
    "tt11358398",
    "tt11777040"
}
