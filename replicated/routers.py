import random
import threading

from django.conf import settings

DATABASE_SLAVES = [dbname for dbname in settings.DATABASES
                   if dbname.startswith('slave')] or ['default']
ALWAYS_MASTER_MODELS = set()

_locals = threading.local()

def randomize_slave():
    _locals.current_slave = random.choice(DATABASE_SLAVES)

def current_slave():
    return getattr(_locals, 'current_slave', 'default')

def use_slave(value):
    _locals.use_slave = value

def using_slave():
    return getattr(_locals, 'use_slave', False)


class MasterSlaveRouter(object):
    def db_for_read(self, model, **hints):
        if using_slave() and model not in ALWAYS_MASTER_MODELS:
            return current_slave()
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'
