import os
from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = True
DATABASES = settings.DATABASES

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static','static_root')

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static','static_dirs'),

# )

# MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static','media')

# MEDIA_URL = '/media/'


# # # Simplified static file serving.
# # # https://warehouse.python.org/project/whitenoise/

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'