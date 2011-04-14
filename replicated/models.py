from replicated import routers

# Don't try slave for Session model
from django.contrib.sessions.models import Session
routers.ALWAYS_MASTER_MODELS.add(Session)
