import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for row in phones:
            release_date = datetime.strptime(row['release_date'], '%Y-%m-%d').date()
            lte_exists = row['lte_exists'].lower() in ('true', '1', 'yes')

            phone = Phone(
                id=int(row['id']),
                name=row['name'],
                price=row['price'],
                image=row['image'],
                release_date=release_date,
                lte_exists=lte_exists
            )
            phone.save()