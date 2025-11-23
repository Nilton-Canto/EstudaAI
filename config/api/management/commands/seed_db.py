import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Loads data from backend/db/seeds.sql into the database"

    def handle(self, *args, **kwargs):
        # BASE_DIR is 'config/', so we go up one level to reach the repo root
        file_path = settings.BASE_DIR.parent / "backend" / "db" / "seeds.sql"

        if not file_path.exists():
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        self.stdout.write(f"Reading seeds from: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            sql = f.read()

        try:
            with connection.cursor() as cursor:
                # SQLite specific method to execute a script with multiple statements
                if connection.vendor == "sqlite":
                    cursor.executescript(sql)
                else:
                    # For other databases, we might need to split statements or use a different approach
                    # But for this project, we know it's SQLite
                    cursor.execute(sql)

            self.stdout.write(self.style.SUCCESS("Successfully loaded seeds.sql"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error executing SQL: {e}"))
            self.stdout.write(
                self.style.WARNING(
                    "Hint: If the error is about 'UNIQUE constraint failed', it means the data is already there."
                )
            )
