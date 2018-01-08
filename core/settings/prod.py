from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'amaris.framanmag.com'
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')