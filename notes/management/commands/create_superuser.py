from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = 'Anubis'
        password = '123'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, 'email@example.com', password)
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
        else:
            self.stdout.write('Superuser already exists.')