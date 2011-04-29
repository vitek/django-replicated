from django.db import connection as master_connection
from replicated.routers import get_slave_connection

