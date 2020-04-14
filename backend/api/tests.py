from django.test import TestCase

# Create your tests here.
from django.conf import settings

app_installed = 'api' in settings.INSTALLED_APPS

print('cai', app_installed)