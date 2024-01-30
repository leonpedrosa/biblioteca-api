import django.db.utils
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import ExtendUser


class Command(BaseCommand):
    help = 'Create superuser'

    def add_arguments(self, parser):
        parser.add_argument(
            '-u', '--username',
            help='Username for the superuser, default is admin@admin.com.br',
            default='admin@admin.com.br'
        )
        parser.add_argument(
            '-e', '--email',
            help='Email for the superuser, default is admin@admin.com.br',
            default='admin@admin.com.br'
        )
        parser.add_argument(
            '-p', '--password',
            help='Password for the superuser',
            required=True
        )
        parser.add_argument(
            '-d', '--document',
            help='Document for the superuser, default is 00000000000',
            default='00000000000'
        )

    def handle(self, *args, **options):
        User = get_user_model()
        try:
            u = User.objects.create_superuser(
                username=options['username'],
                email=options['email'],
                password=options['password']
            )
            ExtendUser.objects.create(
                user=u,
                document=options['document']
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        except django.db.utils.IntegrityError:
            self.stderr.write(self.style.ERROR('User with this email already exists'))
        except Exception as error:
            self.stderr.write(self.style.ERROR(f'Error, super user not created: {error}'))