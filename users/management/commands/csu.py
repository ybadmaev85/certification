from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='cool.badmaev@bk.ru',
            name='Victor',
            phone='+79615457453',
            is_staff=True,
            is_superuser=True,
            is_active=True

        )

        user.set_password('qwe123zxc')
        user.save()
        print('superuser created')
