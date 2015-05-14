__author__ = 'darek'

DEBUG = True

TEMPLATE_DIRS = (
    '/Users/darek/src/food/webapp/webapp/templates/',
)

STATICFILES_DIRS = (
    '/Users/darek/src/food/webapp/webapp/static/',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'food',
        'USER': 'postgres',
        'PASSWORD': 'wertykulator',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# email configuration
EMAIL_HOST = 'mail.dariuszwalczak.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'contact@dariuszwalczak.com'
EMAIL_HOST_PASSWORD = '93WibOoo'
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = 'Food <contact@dariuszwalczak.com>'
NOTIFICATION_QUEUE_ALL = True

