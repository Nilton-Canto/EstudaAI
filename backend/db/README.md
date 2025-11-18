# EstudaAI — Banco de Dados (MySQL 8)

Passo a passo para subir o MySQL, criar o schema e aplicar seeds.

## 0) Pré-requisito
- Docker Desktop instalado **OU** MySQL 8 instalado localmente.

## 1) Subir MySQL com Docker
Na raiz do projeto (onde está `docker-compose.yml`):
```bash
docker compose up -d
```
Isso cria um MySQL acessível em `localhost:3306` com:
- banco: `estudaai`
- usuário: `estuda`
- senha: `estuda`

## 2) Aplicar o schema
```bash
docker exec -i estudaai-mysql   mysql -uroot -proot estudaai < backend/db/schema.sql
```

## 3) (Opcional) Aplicar seeds
```bash
docker exec -i estudaai-mysql   mysql -uroot -proot estudaai < backend/db/seeds.sql
```

## 4) Testar conexão
Entre no container:
```bash
docker exec -it estudaai-mysql mysql -uroot -proot
```
No prompt do MySQL:
```sql
USE estudaai;
SHOW TABLES;
SELECT COUNT(*) FROM subjects;
```

## 5) Integração no back-end
Configure sua variável:
```
DATABASE_URL="mysql://estuda:estuda@localhost:3306/estudaai"
```
E use seu ORM (Prisma/TypeORM) apontando para esse banco (não habilite `synchronize` se já aplicou o schema).

## 6) Fluxo de Git
Crie a branch e faça a PR para `develop`:
```bash
git checkout -b feature/modelagem-banco-dados
# adicione estes arquivos ao seu repositório e commite
git add .
git commit -m "feat(db): add MySQL schema, seeds and docker-compose"
git push origin feature/modelagem-banco-dados
# abra PR: feature -> develop
```
