from api.models import Area
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

Usuario = get_user_model()


class Command(BaseCommand):
    help = "Popula o banco de dados com dados iniciais de teste usando ORM do Django"

    def handle(self, *args, **kwargs):
        self.stdout.write("🌱 Iniciando seed do banco de dados...")

        # Criar áreas de conhecimento
        areas_data = [
            {
                "nome": "Tecnologia da Informação",
                "descricao": "Área relacionada a desenvolvimento de software, sistemas e infraestrutura de TI",
                "icone": "💻",
                "cor": "#4f46e5",
            },
            {
                "nome": "Engenharia",
                "descricao": "Área de engenharias em geral, incluindo elétrica, mecânica, civil, etc.",
                "icone": "⚙️",
                "cor": "#f59e0b",
            },
            {
                "nome": "Ciências Exatas",
                "descricao": "Matemática, Física, Química e áreas correlatas",
                "icone": "🔬",
                "cor": "#10b981",
            },
            {
                "nome": "Administração e Negócios",
                "descricao": "Gestão, empreendedorismo, marketing e áreas relacionadas",
                "icone": "📊",
                "cor": "#ef4444",
            },
        ]

        for area_data in areas_data:
            area, created = Area.objects.get_or_create(
                nome=area_data["nome"],
                defaults={
                    "descricao": area_data["descricao"],
                    "icone": area_data["icone"],
                    "cor": area_data["cor"],
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Área criada: {area.nome}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️  Área já existe: {area.nome}"))

        # Criar usuário de teste (se não existir)
        if not Usuario.objects.filter(username="demo").exists():
            Usuario.objects.create_user(
                username="demo",
                email="demo@estudaai.com",
                password="demo123",
                nome="Usuário Demo",
                universidade="Universidade Mackenzie",
                curso="Engenharia da Computação",
                ano_formatura=2028,
                idade=22,
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "✅ Usuário demo criado (username: demo, senha: demo123)"
                )
            )
        else:
            self.stdout.write(self.style.WARNING("⚠️  Usuário demo já existe"))

        self.stdout.write(self.style.SUCCESS("\n🎉 Seed concluído com sucesso!"))
