from django.core.management.base import BaseCommand
from ...models import Products

import csv
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        """Handles what to do"""
        self.populate_products()

    def populate_products(self):
        """Populate products with their price"""
        data_path = 'django_tuts/forms_tuts/Data/Product Price List.csv'
        working_dir = os.path.dirname(os.getcwd())
        csv_file = os.path.join(working_dir, data_path)
        with open(csv_file) as csvfile:
            product_reader  = csv.reader(csvfile, delimiter=',')
            i = 0
            for row in product_reader:
                if i > 0:
                    price = row[0]
                    name = row[1]
                    try:
                        prod, _ = Products.objects.get_or_create(price=price, name=name)
                    except Exception as e:
                        pass
                i += 1