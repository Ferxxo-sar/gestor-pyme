from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Crea un superusuario admin si no existe'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                password='admin'
            )
            self.stdout.write(self.style.SUCCESS('Superusuario "admin" creado exitosamente'))
        else:
            self.stdout.write(self.style.WARNING('El superusuario "admin" ya existe'))
