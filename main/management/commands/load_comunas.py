import csv
from django.core.management.base import BaseCommand
from main.models import Comuna

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    archivo = open('data/comunas.csv', encoding="utf-8")
    reader = csv.reader(archivo, delimiter=';')
    next(reader)

    for fila in reader:
      Comuna.objects.create(nombre=fila[0], cod=fila[1], region_id=fila[3])
