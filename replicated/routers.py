from random import random
import threading

from django.conf import settings
import django.db

DATABASE_SLAVES = []
TOTAL_WEIGHT = 0
ALWAYS_MASTER_MODELS = set()

for dbname, params in settings.DATABASES.iteritems():
    if not dbname.startswith('slave'):
        continue
    weight = params.get('WEIGHT', 1)
    DATABASE_SLAVES.append((dbname, weight))
    TOTAL_WEIGHT += weight

_locals = threading.local()

def randomize_slave():
    r = TOTAL_WEIGHT * random()
    for dbname, weight in DATABASE_SLAVES:
        if r > weight:
            r -= weight
        else:
            _locals.current_slave = dbname
            return
    _locals.current_slave = 'default'

def current_slave():
    return getattr(_locals, 'current_slave', 'default')

def use_slave(value):
    _locals.use_slave = value

def using_slave():
    return getattr(_locals, 'use_slave', False)

def get_slave_connection():
    """Get slave connection if using_slave() is True."""
    if using_slave():
        return django.db.connections[current_slave()]
    return django.db.connection


class MasterSlaveRouter(object):
    def db_for_read(self, model, **hints):
        if using_slave() and model not in ALWAYS_MASTER_MODELS:
            return current_slave()
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'
