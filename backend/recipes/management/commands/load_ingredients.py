import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка ингредиентов из файла ingredients.csv'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help='Путь к файлу')

    def handle(self, *args, **options):
        print('Загрузка...')
        file_path = options['path'] + 'ingredients.csv'
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                name_csv = 0
                unit_of_measurement_csv = 1
                try:
                    obj, created = Ingredient.objects.get_or_create(
                        name=row[name_csv],
                        unit_of_measurement=row[unit_of_measurement_csv],
                    )
                    if not created:
                        print(f'Ингредиент {obj} уже есть в базе данных.')
                except Exception as err:
                    print(f'Ошибка в строке {row}: {err}')

        print('Данные успешно загружены.')
