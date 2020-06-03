import csv

from django.core.management.base import BaseCommand
from phones.models import Phone

import pandas as pd

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                print(line)
                p = Phone()
                p.name=line[1]
                p.image=line[2]
                p.price=line[3]
                p.release_date=line[4]
                p.lte_exists=line[5]
                p.save()
                pass