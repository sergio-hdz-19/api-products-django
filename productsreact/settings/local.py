from .base import *
from storages.backends.s3boto3 import S3Boto3Storage
from dotenv import load_dotenv
import os

#import environ
# Importa la función load_dotenv desde la biblioteca dotenv
from dotenv import load_dotenv

# Llama a load_dotenv para cargar las variables de entorno desde el archivo .env o example.env
load_dotenv()


#env = environ.Env()
# reading .env file
#environ.Env.read_env()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



ALLOWED_HOSTS = [

    ".vercel.app",

]

CORS_ALLOWED_ORIGINS=[
    'http://localhost:8000',
    'http://localhost:3000',
    'http://localhost:8080',
    'https://main--api-products-django-react.netlify.app/'
]



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR.child('db.sqlite3'),
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
    }
}







# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static'




##DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = os.getenv('AWS_QUERYSTRING_AUTH')


MEDIA_URL = '/media/'
