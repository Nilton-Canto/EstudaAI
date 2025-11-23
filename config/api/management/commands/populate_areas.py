from django.core.management.base import BaseCommand
from api.models import Area

class Command(BaseCommand):
    help = 'Populates initial areas'

    def handle(self, *args, **kwargs):
        areas = [
            {'nome': 'Dados', 'descricao': 'Ciência de Dados, Analytics, Big Data', 'cor': '#3B82F6'},
            {'nome': 'Web', 'descricao': 'Desenvolvimento Web Frontend e Backend', 'cor': '#10B981'},
            {'nome': 'IA', 'descricao': 'Inteligência Artificial e Machine Learning', 'cor': '#8B5CF6'},
        ]

        for area_data in areas:
            area, created = Area.objects.get_or_create(
                nome=area_data['nome'],
                defaults={
                    'descricao': area_data['descricao'],
                    'cor': area_data['cor']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Area "{area.nome}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'Area "{area.nome}" already exists'))
