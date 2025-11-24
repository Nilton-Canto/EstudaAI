import json
import os
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from api.models import Area, TrilhaCurso

Usuario = get_user_model()

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'data', 'trilhas_predefinidas.json')

REQUIRED_AULA_FIELDS = ["titulo", "descricao", "tipo", "duracao"]  # campos mínimos
RICH_FIELDS = ["dificuldade", "objetivos", "recursos"]  # campos enriquecidos


class Command(BaseCommand):
    help = "Popula trilhas pré-definidas lendo JSON externo. Use --dry-run para simular, --refresh para recriar, --only 'titulo' para uma trilha específica."

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true', help='Apenas mostra o que seria feito, sem criar nada')
        parser.add_argument('--refresh', action='store_true', help='Remove trilhas pré-definidas existentes e recria')
        parser.add_argument('--only', type=str, help='Processa apenas a trilha cujo título contenha este texto')

    def carregar_trilhas(self):
        if not os.path.exists(DATA_PATH):
            raise CommandError(f"Arquivo de dados não encontrado: {DATA_PATH}")
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                raise CommandError(f"JSON inválido: {e}")
        if not isinstance(data, list):
            raise CommandError("Estrutura do JSON deve ser uma lista de trilhas")
        return data

    def validar_aulas(self, trilha):
        problemas = []
        conteudo = trilha.get('conteudo', {})
        modulos = conteudo.get('modulos', [])
        for m_idx, modulo in enumerate(modulos):
            aulas = modulo.get('aulas', [])
            for a_idx, aula in enumerate(aulas):
                faltando = [f for f in REQUIRED_AULA_FIELDS if f not in aula]
                riqueza_faltando = [f for f in RICH_FIELDS if f not in aula]
                if faltando:
                    problemas.append(f"[Faltando] {trilha['titulo']} -> M{m_idx+1} A{a_idx+1}: campos {faltando}")
                if riqueza_faltando:
                    # Apenas aviso; não bloqueia
                    problemas.append(f"[Aviso] {trilha['titulo']} -> M{m_idx+1} A{a_idx+1}: faltam campos ricos {riqueza_faltando}")
        return problemas

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        refresh = options['refresh']
        only = options.get('only')

        trilhas = self.carregar_trilhas()
        if only:
            trilhas = [t for t in trilhas if only.lower() in t.get('titulo', '').lower()]
            if not trilhas:
                self.stdout.write(self.style.WARNING(f"Nenhuma trilha corresponde ao filtro --only '{only}'"))
                return

        admin_user, _ = Usuario.objects.get_or_create(
            username="admin_trilhas",
            defaults={
                "email": "admin@estudaai.com",
                "nome": "Administrador de Trilhas",
                "is_staff": True,
                "is_superuser": False,
            }
        )

        if refresh and not dry_run:
            existentes = TrilhaCurso.objects.filter(usuario=admin_user)
            count = existentes.count()
            existentes.delete()
            self.stdout.write(self.style.WARNING(f"Removidas {count} trilhas pré-definidas antigas."))

        total_criadas = 0
        total_ignoradas = 0
        avisos = []

        for trilha_data in trilhas:
            problemas = self.validar_aulas(trilha_data)
            avisos.extend(problemas)
            area_nome = trilha_data.get("area_nome")
            titulo = trilha_data.get("titulo")
            descricao = trilha_data.get("descricao", "")
            conteudo = trilha_data.get("conteudo", {})

            if not area_nome or not titulo:
                self.stdout.write(self.style.ERROR(f"Trilha ignorada por falta de 'area_nome' ou 'titulo': {trilha_data}"))
                total_ignoradas += 1
                continue

            try:
                area = Area.objects.get(nome=area_nome)
            except Area.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Área '{area_nome}' não encontrada. Execute populate_areas."))
                total_ignoradas += 1
                continue

            if dry_run:
                self.stdout.write(f"[Dry-run] Prepararia criação da trilha: {titulo}")
                continue

            trilha, created = TrilhaCurso.objects.get_or_create(
                usuario=admin_user,
                titulo=titulo,
                defaults={
                    "descricao": descricao,
                    "area": area,
                    "conteudo_json": conteudo,
                    "solicitacao_original": "",
                    "ativa": True,
                }
            )

            if created:
                total_criadas += 1
                self.stdout.write(self.style.SUCCESS(f"Criada: {trilha.titulo}"))
            else:
                self.stdout.write(self.style.WARNING(f"Já existe: {trilha.titulo}"))

        if avisos:
            self.stdout.write(self.style.WARNING(f"\nAvisos/Problemas de estrutura ({len(avisos)}):"))
            for msg in avisos:
                self.stdout.write(f" - {msg}")

        resumo = f"Processo finalizado. Criadas={total_criadas} Ignoradas={total_ignoradas} DryRun={'sim' if dry_run else 'não'}"
        self.stdout.write(self.style.SUCCESS(f"\n✅ {resumo}"))
