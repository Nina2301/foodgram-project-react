import csv
import logging
import os

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Загрузка ингредиентов из файла ingredients.csv'

    def handle(self, *args, **options):
        print('Загрузка...')
        file_path = os.path.join(os.path.dirname(__file__), 'ingredients.csv')
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                name_csv = 0
                measurement_unit_csv = 1
                try:
                    obj, created = Ingredient.objects.get_or_create(
                        name=row[name_csv],
                        measurement_unit=row[measurement_unit_csv],
                    )
                    if not created:
                        logger.info(f'Ингредиент {obj} уже есть в базе данных.')
                except UnicodeDecodeError as err:
                    logger.info(f'Ошибка в строке {row}: {err}')
        print('Данные успешно загружены.')
