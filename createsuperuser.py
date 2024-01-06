import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes_api.settings")

import django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'Anubis'
password = '123'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, 'email@example.com', password)
    print('Superuser created.')
else:
    print('Superuser already exists.')