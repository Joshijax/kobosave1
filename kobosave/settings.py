import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '******'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'kobosave.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'creditcards',
    'save',
    'storages',
    'allauth',
    'allauth.account',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kobosave.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'templates', 'allauth')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'kobosave.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'kobosave',
'USER': 'admin',
'PASSWORD': 'treasure12',
'HOST': 'database-2.cgbpxoayuxpw.us-east-2.rds.amazonaws.com',
'PORT': '3306',
'OPTIONS': {
'init_command': "SET sql_mode = 'STRICT_TRANS_TABLES'"
}
}
}
 

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT =  os.path.join(BASE_DIR, 'staticfiles')



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


SITE_ID = 1
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_EMAIL_REQUIRED = True   
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
# REST_SESSION_LOGIN = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_FORM_CLASS = 'save.forms.SignupForm'
ACCOUNT_FORMS = {'login': 'save.forms.LoginForm'}
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/payment-dashboard/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
   
   
EMAIL_HOST_USER = '****'
EMAIL_HOST_PASSWORD = '*****'
EMAIL_USE_TLS = True
MAIL_USE_SSL = False
EMAIL_PORT = 587
 


#S3 BUCKETS CONFIG
USE_S3 = True
if USE_S3:
    AWS_ACCESS_KEY_ID = '****'
    AWS_SECRET_ACCESS_KEY = '****'
    AWS_STORAGE_BUCKET_NAME = 'joshijax'
    # AWS_LOCATION = 'static'
    AWS_S3_SECURE_URLS = False
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # STATIC_LOCATION = 'static'
    # STATICFILES_STORAGE = 'kobosave.storage_backends.StaticStorage'
    AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    # STATICFILES_DIRS = [
    #     os.path.join(BASE_DIR, 'static'),
    # ] 
     
    # STATIC_ROOT = os.path.join(BASE_DIR, 'http://%s.s3.amazonaws.com//static/'  % AWS_STORAGE_BUCKET_NAME)
    # STATIC_URL='https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    # ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
    # STATICFILES_FINDERS = (           'django.contrib.staticfiles.finders.FileSystemFinder',    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # )

    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME  
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    MEDIA_ROOT = 'http://%s.s3.amazonaws.com//media/'  % AWS_STORAGE_BUCKET_NAME 
    DEFAULT_FILE_STORAGE = 'kobosave.storage_backends.PublicMediaStorage'





# '''
# <?xml version="1.0" encoding="UTF-8"?>
# <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
# <CORSRule>
#     <AllowedOrigin>*</AllowedOrigin>
#     <AllowedMethod>GET</AllowedMethod>
#     <AllowedMethod>POST</AllowedMethod>
#     <AllowedMethod>PUT</AllowedMethod>
#     <AllowedHeader>*</AllowedHeader>
# </CORSRule>
# </CORSConfiguration>
# '''