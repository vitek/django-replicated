from replicated import routers


def _replicated(func, use_slave):
    def wrapper(*args, **kwargs):
        saved = routers.using_slave()
        routers.use_slave(use_slave)
        try:
            return func(*args, **kwargs)
        finally:
            routers.use_slave(saved)
    return wrapper

def use_master(func):
    return _replicated(func, False)

def use_slave(func):
    return _replicated(func, True)
