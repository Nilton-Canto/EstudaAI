from api.models import Area
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Populates initial areas"

    def handle(self, *args, **kwargs):
        areas = [
            {
                "nome": "Desenvolvimento Web",
                "descricao": "Desenvolvimento de aplicações web frontend e backend, frameworks modernos e arquitetura web",
                "icone": "🌐",
                "cor": "#10B981",
            },
            {
                "nome": "Ciência de Dados",
                "descricao": "Análise de dados, visualização, estatística, Big Data e ferramentas de analytics",
                "icone": "📊",
                "cor": "#3B82F6",
            },
            {
                "nome": "Inteligência Artificial",
                "descricao": "Machine Learning, Deep Learning, NLP, Computer Vision e aplicações de IA",
                "icone": "🤖",
                "cor": "#8B5CF6",
            },
            {
                "nome": "Soft Skills",
                "descricao": "Comunicação, liderança, trabalho em equipe, gestão de tempo e desenvolvimento pessoal",
                "icone": "💼",
                "cor": "#F59E0B",
            },
            {
                "nome": "Segurança da Informação",
                "descricao": "Cibersegurança, ethical hacking, proteção de dados e compliance",
                "icone": "🔒",
                "cor": "#EF4444",
            },
            {
                "nome": "DevOps e Cloud",
                "descricao": "Infraestrutura como código, CI/CD, containers, Kubernetes e cloud computing",
                "icone": "☁️",
                "cor": "#06B6D4",
            },
        ]

        for area_data in areas:
            area, created = Area.objects.get_or_create(
                nome=area_data["nome"],
                defaults={
                    "descricao": area_data["descricao"],
                    "cor": area_data["cor"],
                    "icone": area_data.get("icone", ""),
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Area "{area.nome}" created'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Area "{area.nome}" already exists')
                )
