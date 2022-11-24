from pathlib import Path
# deploy
import environ

env = environ.Env(
    DEBUG=(bool, True)
)

environ.Env.read_env()

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

# deploy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m#l7g5g3i&+2p928smyen%czx-o!m8x*si(!=i4u9)9jdo@24r'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chart',
    'rest_framework',
    'hitcount',

    'widget_tweaks'
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TSL = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "bekzodbek06062006@gmail.com"
EMAIL_HOST_PASSWORD = "Password2006"
EMAIL_PORT = 587

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation

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

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)

STATICFILES_DIRS =(
    BASE_DIR / "static",
)

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staicfiles'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'chart.MyUser'