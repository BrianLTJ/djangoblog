"""
WSGI config for djangoblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys
 #set VirtualEnv
# sys.path.append("/path/to/site-packages")  

# Set Site Address
# sys.path.append("/path/to/site")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoblog.settings")

application = get_wsgi_application()
