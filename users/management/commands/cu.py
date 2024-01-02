from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            telegram_account='test_user',
            email='victor.badmaef@yandex.ru',
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        user.set_password('qwe123zxc')
        user.save()
