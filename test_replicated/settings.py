# Django settings for test_replicated project.

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'master.db',
    },
    'slave': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'slave1.db',
    },
}


DATABASE_ROUTERS = ('replicated.routers.MasterSlaveRouter',)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'replicated.middleware.MasterSlaveMiddleware',
)

ROOT_URLCONF = 'test_replicated.urls'

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'replicated',
    'testapp',
)
