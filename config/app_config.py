import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env.read_env(f'{BASE_DIR}/.env')

# FILE UPLOAD PATH
PROFILE_UPLOAD_PATH = 'uploads/profile'
BUSINESS_AVATAR_UPLOAD_PATH = 'uploads/business'
DOCUMENT_UPLOAD_PATH = 'uploads/documents'
PRODUCT_IMAGE_UPLOAD_PATH = 'uploads/products'

NUMBERS = '0123456789'
ALPHA_NUM = f'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{NUMBERS}'

# EMAIL ADN USERNAME OF SERVER ADMIN USER
SERVER_MAIL = 'sudouser1443@gmail.com'
SERVER_ADMIN_NAME = 'Confidence Yobo'

# DATABASE CONFIG
DB_ENGINE = env('DB_ENGINE')
DB_NAME = env('DB_NAME')
DB_USER = env('DB_USER')
DB_PASSWORD = env('DB_PASSWORD')
DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')

DEBUG = env('DEBUG_MODE', default=False)
SECRET_KEY = env('SECRET_KEY') or os.environ.get('SECRET_KEY')

TIME_ZONE = env('TIME_ZONE')

# EMAIL CONFIG
EMAIL_USE_TLS = env('MAIL_USE_TLS')
EMAIL_HOST = env('MAIL_HOST')
EMAIL_HOST_USER = env('MAIL_USER')
EMAIL_HOST_PASSWORD = env('MAIL_PASSWORD')
EMAIL_PORT = env('MAIL_PORT')

CACHE_KEY_PREFIX = env('CACHE_KEY_PREFIX')

DJANGO_SETTINGS_MODULE = env('DJANGO_SETTINGS_MODULE')
