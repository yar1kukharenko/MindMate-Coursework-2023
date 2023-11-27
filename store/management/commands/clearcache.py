import os
import shutil

from django.core.cache import cache
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Очищает кэш и временные файлы'

    def handle(self, *args, **options):
        # Очистка кэша Django
        cache.clear()
        self.stdout.write(self.style.SUCCESS('Кэш успешно очищен.'))

        # Опционально: Очистка определенной директории с временными файлами
        # Например, 'temp_dir/' это путь к вашей директории с временными файлами
        temp_dir = 'temp_dir/'
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            os.makedirs(temp_dir)
            self.stdout.write(self.style.SUCCESS('Временные файлы успешно удалены.'))
