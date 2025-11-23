BEGIN TRANSACTION;
CREATE TABLE "api_area" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nome" varchar(100) NOT NULL UNIQUE, "descricao" text NOT NULL, "icone" varchar(50) NOT NULL, "cor" varchar(7) NOT NULL, "ativa" bool NOT NULL, "data_criacao" datetime NOT NULL, "data_atualizacao" datetime NOT NULL);
INSERT INTO "api_area" VALUES(1,'TI do Niltinho','HMMMMMM','💻','#4ce6db',1,'2025-11-16 03:33:54.203810','2025-11-16 04:09:00.265729');
INSERT INTO "api_area" VALUES(2,'Eletrica','AIAIA','💡','#4f4e74',1,'2025-11-16 05:29:41.473073','2025-11-16 05:35:36.554335');
CREATE TABLE "api_gemini_trilhacurso" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(255) NOT NULL, "descricao" text NOT NULL, "solicitacao_original" text NOT NULL, "conteudo_json" text NOT NULL CHECK ((JSON_VALID("conteudo_json") OR "conteudo_json" IS NULL)), "data_criacao" datetime NOT NULL, "data_atualizacao" datetime NOT NULL, "ativa" bool NOT NULL, "usuario_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "api_gemini_trilhacurso" VALUES(1,'Python para iniciantes','POO','POO','{"modules": [{"id": 1, "title": "Introdu\u00e7\u00e3o ao Python", "description": "Fundamentos da linguagem Python", "duration": "1 semana", "lessons": [{"id": 1, "title": "O que \u00e9 Python?", "type": "theory", "content": "Python \u00e9 uma linguagem de programa\u00e7\u00e3o...", "duration": "30min", "resources": [{"type": "video", "url": "https://exemplo.com/video1", "title": "Introdu\u00e7\u00e3o ao Python"}, {"type": "text", "content": "Material de leitura sobre Python..."}]}, {"id": 2, "title": "Primeiro programa em Python", "type": "practical", "content": "Vamos criar nosso primeiro programa...", "duration": "45min", "exercises": [{"id": 1, "question": "Escreva um programa que imprima ''Hello World''", "code_template": "# Escreva seu c\u00f3digo aqui\nprint()", "expected_output": "Hello World", "hints": ["Use a fun\u00e7\u00e3o print()", "Coloque o texto entre aspas"]}]}], "quiz": {"questions": [{"id": 1, "question": "O que significa Python?", "type": "multiple_choice", "options": ["Uma cobra", "Uma linguagem de programa\u00e7\u00e3o", "Um sistema operacional", "Um banco de dados"], "correct_answer": 1, "explanation": "Python \u00e9 uma linguagem de programa\u00e7\u00e3o de alto n\u00edvel."}]}}, {"id": 2, "title": "Vari\u00e1veis e Tipos de Dados", "description": "Aprenda sobre vari\u00e1veis e tipos b\u00e1sicos", "duration": "1 semana", "lessons": [{"id": 3, "title": "Criando vari\u00e1veis", "type": "theory", "content": "Em Python, voc\u00ea pode criar vari\u00e1veis...", "duration": "25min", "code_examples": [{"title": "Exemplo de vari\u00e1veis", "code": "nome = ''Jo\u00e3o''\nidade = 25\naltura = 1.75", "explanation": "Aqui criamos tr\u00eas vari\u00e1veis de tipos diferentes"}]}]}], "prerequisites": ["Conhecimento b\u00e1sico de l\u00f3gica", "Familiaridade com computadores"], "learning_objectives": ["Entender sintaxe b\u00e1sica do Python", "Criar programas simples", "Trabalhar com vari\u00e1veis e tipos de dados"], "final_project": {"title": "Calculadora Simples", "description": "Crie uma calculadora que realize opera\u00e7\u00f5es b\u00e1sicas", "requirements": ["Interface de linha de comando", "Opera\u00e7\u00f5es: +, -, *, /", "Tratamento de erros b\u00e1sico"], "evaluation_criteria": ["Funcionalidade", "Qualidade do c\u00f3digo", "Tratamento de erros"]}}','2025-09-22 21:54:53.774895','2025-09-22 21:54:53.774895',1,2);
INSERT INTO "api_gemini_trilhacurso" VALUES(2,'Python para Análise de Dados: Uma Trilha Completa','Esta trilha de aprendizado foi projetada para guiá-lo desde os fundamentos do Python até a aplicação de técnicas de análise de dados. Ela cobre desde a sintaxe básica até bibliotecas avançadas como Pandas, NumPy e Matplotlib, com foco em projetos práticos e aplicáveis. Ideal para iniciantes sem experiência prévia em programação ou análise de dados.','Quero aprender Python para análise de dados','{"titulo": "Python para An\u00e1lise de Dados: Uma Trilha Completa", "descricao": "Esta trilha de aprendizado foi projetada para gui\u00e1-lo desde os fundamentos do Python at\u00e9 a aplica\u00e7\u00e3o de t\u00e9cnicas de an\u00e1lise de dados. Ela cobre desde a sintaxe b\u00e1sica at\u00e9 bibliotecas avan\u00e7adas como Pandas, NumPy e Matplotlib, com foco em projetos pr\u00e1ticos e aplic\u00e1veis. Ideal para iniciantes sem experi\u00eancia pr\u00e9via em programa\u00e7\u00e3o ou an\u00e1lise de dados.", "nivel": "Iniciante", "duracao_total": "12 semanas", "modulos": [{"numero": 1, "titulo": "Introdu\u00e7\u00e3o ao Python e Configura\u00e7\u00e3o do Ambiente", "descricao": "Este m\u00f3dulo cobre os fundamentos da linguagem Python, a instala\u00e7\u00e3o do ambiente de desenvolvimento (Anaconda) e os primeiros passos na programa\u00e7\u00e3o.", "duracao": "1 semana", "topicos": ["O que \u00e9 Python e por que us\u00e1-lo para an\u00e1lise de dados", "Instala\u00e7\u00e3o do Anaconda e configura\u00e7\u00e3o do ambiente", "IDEs para Python (Jupyter Notebook, VS Code)", "Tipos de dados b\u00e1sicos (inteiros, floats, strings, booleanos)", "Operadores aritm\u00e9ticos e l\u00f3gicos", "Vari\u00e1veis e atribui\u00e7\u00f5es"], "recursos": [{"tipo": "video", "titulo": "Python para Iniciantes - Curso Completo (Gratuito)", "descricao": "V\u00eddeo introdut\u00f3rio sobre Python com foco em iniciantes."}, {"tipo": "livro", "titulo": "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming", "descricao": "Um livro excelente para aprender Python de forma pr\u00e1tica."}, {"tipo": "artigo", "titulo": "Python Setup and Usage", "descricao": "Documenta\u00e7\u00e3o oficial sobre a instala\u00e7\u00e3o e uso do Python."}], "atividades_praticas": ["Instalar o Anaconda e o Jupyter Notebook", "Escrever um programa simples que imprime ''Ol\u00e1, Mundo!''", "Criar vari\u00e1veis e realizar opera\u00e7\u00f5es aritm\u00e9ticas", "Resolver exerc\u00edcios b\u00e1sicos de l\u00f3gica"]}, {"numero": 2, "titulo": "Estruturas de Dados e Controle de Fluxo", "descricao": "Este m\u00f3dulo aborda as principais estruturas de dados em Python e as estruturas de controle de fluxo, essenciais para a cria\u00e7\u00e3o de programas mais complexos.", "duracao": "2 semanas", "topicos": ["Listas: cria\u00e7\u00e3o, acesso, manipula\u00e7\u00e3o", "Tuplas: cria\u00e7\u00e3o, acesso", "Dicion\u00e1rios: cria\u00e7\u00e3o, acesso, manipula\u00e7\u00e3o", "Sets: cria\u00e7\u00e3o, opera\u00e7\u00f5es", "Estruturas de controle: if, else, elif", "Loops: for, while", "Comprehensions (list, dictionary, set)"], "recursos": [{"tipo": "video", "titulo": "Python Data Structures Tutorial", "descricao": "Tutorial sobre as estruturas de dados em Python."}, {"tipo": "curso", "titulo": "Codecademy: Learn Python 3", "descricao": "Curso interativo sobre Python com exerc\u00edcios pr\u00e1ticos."}, {"tipo": "livro", "titulo": "Automate the Boring Stuff with Python", "descricao": "Livro com foco em automa\u00e7\u00e3o de tarefas com Python, \u00fatil para aplicar o aprendizado de estruturas de dados."}], "atividades_praticas": ["Criar listas, dicion\u00e1rios e sets e manipul\u00e1-los", "Escrever programas que usam estruturas condicionais (if/else)", "Implementar loops para iterar sobre listas e dicion\u00e1rios", "Resolver problemas que envolvam estruturas de dados e controle de fluxo."]}, {"numero": 3, "titulo": "Fun\u00e7\u00f5es e Programa\u00e7\u00e3o Orientada a Objetos (POO)", "descricao": "Este m\u00f3dulo introduz o conceito de fun\u00e7\u00f5es, modulariza\u00e7\u00e3o de c\u00f3digo e os princ\u00edpios b\u00e1sicos da Programa\u00e7\u00e3o Orientada a Objetos.", "duracao": "2 semanas", "topicos": ["Definindo e chamando fun\u00e7\u00f5es", "Par\u00e2metros e argumentos", "Retorno de valores", "Escopo de vari\u00e1veis", "Introdu\u00e7\u00e3o \u00e0 POO: Classes e objetos", "Atributos e m\u00e9todos", "Heran\u00e7a e polimorfismo (conceitos b\u00e1sicos)"], "recursos": [{"tipo": "video", "titulo": "Python Functions Tutorial", "descricao": "Tutorial sobre fun\u00e7\u00f5es em Python."}, {"tipo": "livro", "titulo": "Effective Python: 90 Specific Ways to Write Better Python", "descricao": "Livro com dicas e boas pr\u00e1ticas para escrever c\u00f3digo Python mais eficiente."}, {"tipo": "curso", "titulo": "Object-Oriented Programming in Python", "descricao": "Curso online sobre programa\u00e7\u00e3o orientada a objetos em Python."}], "atividades_praticas": ["Escrever fun\u00e7\u00f5es para realizar tarefas espec\u00edficas", "Criar classes e objetos simples", "Implementar heran\u00e7a e polimorfismo", "Criar um programa que utilize fun\u00e7\u00f5es e POO para resolver um problema."]}, {"numero": 4, "titulo": "NumPy: Computa\u00e7\u00e3o Num\u00e9rica com Python", "descricao": "Este m\u00f3dulo apresenta a biblioteca NumPy, fundamental para realizar opera\u00e7\u00f5es num\u00e9ricas eficientes com arrays multidimensionais.", "duracao": "2 semanas", "topicos": ["Introdu\u00e7\u00e3o ao NumPy", "Arrays NumPy: cria\u00e7\u00e3o, indexa\u00e7\u00e3o, slicing", "Tipos de dados em NumPy", "Opera\u00e7\u00f5es aritm\u00e9ticas com arrays", "Fun\u00e7\u00f5es universais (ufuncs)", "Broadcasting", "\u00c1lgebra linear b\u00e1sica com NumPy"], "recursos": [{"tipo": "video", "titulo": "NumPy Tutorial for Beginners", "descricao": "Tutorial introdut\u00f3rio sobre NumPy."}, {"tipo": "livro", "titulo": "Python Data Science Handbook", "descricao": "Livro completo sobre ci\u00eancia de dados em Python, com foco em NumPy e Pandas."}, {"tipo": "artigo", "titulo": "NumPy Documentation", "descricao": "Documenta\u00e7\u00e3o oficial do NumPy."}], "atividades_praticas": ["Criar arrays NumPy de diferentes formas e tamanhos", "Realizar opera\u00e7\u00f5es aritm\u00e9ticas com arrays", "Utilizar fun\u00e7\u00f5es universais para transformar arrays", "Resolver problemas de \u00e1lgebra linear com NumPy"]}, {"numero": 5, "titulo": "Pandas: An\u00e1lise de Dados com Python", "descricao": "Este m\u00f3dulo aborda a biblioteca Pandas, essencial para manipula\u00e7\u00e3o e an\u00e1lise de dados tabulares.", "duracao": "3 semanas", "topicos": ["Introdu\u00e7\u00e3o ao Pandas", "Series: cria\u00e7\u00e3o, indexa\u00e7\u00e3o, manipula\u00e7\u00e3o", "DataFrames: cria\u00e7\u00e3o, leitura de dados (CSV, Excel)", "Indexa\u00e7\u00e3o e sele\u00e7\u00e3o de dados em DataFrames", "Limpeza e tratamento de dados faltantes", "Agrupamento e agrega\u00e7\u00e3o de dados", "Merge e join de DataFrames", "Opera\u00e7\u00f5es com strings e datas", "Pivot tables"], "recursos": [{"tipo": "video", "titulo": "Pandas Tutorial for Beginners", "descricao": "Tutorial introdut\u00f3rio sobre Pandas."}, {"tipo": "livro", "titulo": "Python for Data Analysis", "descricao": "Livro detalhado sobre an\u00e1lise de dados com Pandas."}, {"tipo": "artigo", "titulo": "Pandas Documentation", "descricao": "Documenta\u00e7\u00e3o oficial do Pandas."}], "atividades_praticas": ["Criar DataFrames a partir de diferentes fontes de dados", "Limpar e tratar dados faltantes em DataFrames", "Realizar opera\u00e7\u00f5es de agrupamento e agrega\u00e7\u00e3o", "Merge e join de DataFrames", "Analisar dados reais utilizando Pandas."]}, {"numero": 6, "titulo": "Matplotlib: Visualiza\u00e7\u00e3o de Dados", "descricao": "Este m\u00f3dulo apresenta a biblioteca Matplotlib, utilizada para criar visualiza\u00e7\u00f5es de dados como gr\u00e1ficos e tabelas.", "duracao": "2 semanas", "topicos": ["Introdu\u00e7\u00e3o ao Matplotlib", "Criando gr\u00e1ficos b\u00e1sicos (linhas, barras, dispers\u00e3o)", "Personaliza\u00e7\u00e3o de gr\u00e1ficos (t\u00edtulos, r\u00f3tulos, cores)", "Subplots", "Visualiza\u00e7\u00e3o de dados com Pandas", "Tipos de gr\u00e1ficos mais comuns para an\u00e1lise de dados (histogramas, boxplots)"], "recursos": [{"tipo": "video", "titulo": "Matplotlib Tutorial for Beginners", "descricao": "Tutorial introdut\u00f3rio sobre Matplotlib."}, {"tipo": "artigo", "titulo": "Matplotlib Documentation", "descricao": "Documenta\u00e7\u00e3o oficial do Matplotlib."}, {"tipo": "artigo", "titulo": "Seaborn Documentation", "descricao": "Documenta\u00e7\u00e3o da biblioteca Seaborn (opcional, mas recomendada para visualiza\u00e7\u00f5es mais avan\u00e7adas)."}], "atividades_praticas": ["Criar diferentes tipos de gr\u00e1ficos utilizando Matplotlib", "Personalizar gr\u00e1ficos para torn\u00e1-los mais informativos", "Visualizar dados de DataFrames utilizando Matplotlib", "Criar visualiza\u00e7\u00f5es para comunicar insights de dados."]}], "projeto_final": "An\u00e1lise explorat\u00f3ria de um conjunto de dados real (ex: dados de vendas, dados de redes sociais, dados de sa\u00fade). O projeto dever\u00e1 incluir limpeza de dados, an\u00e1lise estat\u00edstica b\u00e1sica, visualiza\u00e7\u00e3o de dados e apresenta\u00e7\u00e3o dos principais insights encontrados.", "recursos_complementares": ["Scikit-learn Documentation (para aprendizado de m\u00e1quina futuro)", "Kaggle (para encontrar datasets e desafios de an\u00e1lise de dados)"]}','2025-10-22 19:05:29.026833','2025-10-22 19:05:29.026833',1,3);
INSERT INTO "api_gemini_trilhacurso" VALUES(3,'Do Zero ao Bolo de Chocolate Perfeito: Uma Trilha de Aprendizado','Esta trilha de aprendizado foi projetada para guiá-lo desde os conceitos básicos da culinária até a criação de um bolo de chocolate delicioso e perfeito. Aprenda técnicas essenciais, domine os ingredientes e pratique para se tornar um mestre na arte da confeitaria de bolos de chocolate.','Quero fazer um bolo de chocolate','{"titulo": "Do Zero ao Bolo de Chocolate Perfeito: Uma Trilha de Aprendizado", "descricao": "Esta trilha de aprendizado foi projetada para gui\u00e1-lo desde os conceitos b\u00e1sicos da culin\u00e1ria at\u00e9 a cria\u00e7\u00e3o de um bolo de chocolate delicioso e perfeito. Aprenda t\u00e9cnicas essenciais, domine os ingredientes e pratique para se tornar um mestre na arte da confeitaria de bolos de chocolate.", "nivel": "Iniciante", "duracao_total": "4 semanas", "modulos": [{"numero": 1, "titulo": "Introdu\u00e7\u00e3o \u00e0 Confeitaria e Ingredientes Essenciais", "descricao": "Neste m\u00f3dulo, voc\u00ea aprender\u00e1 os fundamentos da confeitaria, desde a higiene e seguran\u00e7a alimentar at\u00e9 a identifica\u00e7\u00e3o e fun\u00e7\u00e3o dos principais ingredientes usados em bolos de chocolate.", "duracao": "1 semana", "topicos": ["Higiene e Seguran\u00e7a Alimentar na Cozinha", "Equipamentos Essenciais para Fazer Bolos", "Farinhas: Tipos, Propriedades e Usos", "A\u00e7\u00facares: Tipos, Fun\u00e7\u00f5es e Impacto no Bolo", "Gorduras: Manteiga, \u00d3leo e seus Efeitos", "Ovos: Estrutura, Liga\u00e7\u00e3o e Aera\u00e7\u00e3o", "Chocolate: Tipos, Qualidade e Prepara\u00e7\u00e3o", "Fermentos Qu\u00edmicos: Bicarbonato de S\u00f3dio e Fermento em P\u00f3"], "recursos": [{"tipo": "artigo", "titulo": "Guia Completo de Ingredientes para Bolos", "descricao": "Um artigo detalhado sobre as propriedades e fun\u00e7\u00f5es de cada ingrediente em uma receita de bolo."}, {"tipo": "video", "titulo": "Higiene e Seguran\u00e7a Alimentar na Cozinha Dom\u00e9stica", "descricao": "Um v\u00eddeo curto e informativo sobre as melhores pr\u00e1ticas de higiene na cozinha."}], "atividades_praticas": ["Identifique e organize os ingredientes b\u00e1sicos para um bolo de chocolate em sua cozinha.", "Limpe e organize sua esta\u00e7\u00e3o de trabalho, garantindo a higiene e a seguran\u00e7a alimentar."]}, {"numero": 2, "titulo": "T\u00e9cnicas de Preparo e Mistura", "descricao": "Este m\u00f3dulo ensinar\u00e1 as t\u00e9cnicas b\u00e1sicas de preparo e mistura, incluindo cremage, mistura de l\u00edquidos e secos e a import\u00e2ncia da temperatura dos ingredientes.", "duracao": "1 semana", "topicos": ["Medi\u00e7\u00e3o Precisa de Ingredientes (pesagem vs. volume)", "T\u00e9cnica de Cremagem: A\u00e7\u00facar e Gordura", "Incorpora\u00e7\u00e3o de Ovos: Passo a Passo", "Mistura de Ingredientes Secos: Peneirar e Homogeneizar", "Alternando Ingredientes Secos e L\u00edquidos", "Evitando o Excesso de Mistura (Gl\u00faten)", "A Import\u00e2ncia da Temperatura dos Ingredientes", "Preparo da Forma: Untar e Enfarinhar/Papel Manteiga"], "recursos": [{"tipo": "video", "titulo": "T\u00e9cnicas de Mistura para Bolos: Cremagem e Mais", "descricao": "Demonstra\u00e7\u00e3o visual das t\u00e9cnicas de mistura mais importantes."}, {"tipo": "livro", "titulo": "The Cake Bible (Rose Levy Beranbaum)", "descricao": "Um livro de refer\u00eancia abrangente sobre t\u00e9cnicas de panifica\u00e7\u00e3o."}], "atividades_praticas": ["Pratique a t\u00e9cnica de cremage com diferentes tipos de gordura (manteiga, margarina, \u00f3leo).", "Experimente a incorpora\u00e7\u00e3o de ovos em diferentes temperaturas."]}, {"numero": 3, "titulo": "Assando o Bolo de Chocolate Perfeito", "descricao": "Este m\u00f3dulo cobre a temperatura do forno, tempo de cozimento, testes de cozimento e resfriamento adequado para evitar bolos secos ou mal cozidos.", "duracao": "1 semana", "topicos": ["Temperatura Ideal do Forno para Bolos de Chocolate", "Posicionamento da Grade do Forno", "Tempo de Cozimento: Fatores que Influenciam", "Testes de Cozimento: Palito, Toque e Apar\u00eancia", "Resfriamento na Forma vs. Resfriamento em Grade", "Evitando Bolos Secos: Dicas e Truques", "Resolvendo Problemas Comuns de Assamento", "Armazenamento Adequado de Bolos de Chocolate"], "recursos": [{"tipo": "artigo", "titulo": "Guia Definitivo para Assar Bolos Perfeitos", "descricao": "Um artigo que aborda todos os aspectos do processo de assamento."}, {"tipo": "video", "titulo": "Como Saber se o Bolo Est\u00e1 Assado", "descricao": "Um v\u00eddeo curto mostrando diferentes testes de cozimento."}], "atividades_praticas": ["Asse um bolo de chocolate simples e registre a temperatura do forno e o tempo de cozimento.", "Teste diferentes m\u00e9todos de resfriamento para verificar o impacto na umidade do bolo."]}, {"numero": 4, "titulo": "Coberturas e Decora\u00e7\u00f5es para Bolo de Chocolate", "descricao": "Aprenda a fazer ganaches, buttercream, caldas e outras coberturas deliciosas para complementar seu bolo de chocolate. Explore t\u00e9cnicas de decora\u00e7\u00e3o simples e elegantes.", "duracao": "1 semana", "topicos": ["Ganache de Chocolate: Propor\u00e7\u00f5es e Varia\u00e7\u00f5es", "Buttercream: Tipos, Texturas e Sabores", "Calda de Chocolate: Simples e Sofisticada", "Glac\u00ea Real: Preparo e Aplica\u00e7\u00f5es", "Decora\u00e7\u00e3o com Raspas de Chocolate", "Utiliza\u00e7\u00e3o de Frutas Frescas na Decora\u00e7\u00e3o", "T\u00e9cnicas B\u00e1sicas de Bicos de Confeitar", "Montagem e Finaliza\u00e7\u00e3o do Bolo"], "recursos": [{"tipo": "curso", "titulo": "Curso Online de Decora\u00e7\u00e3o de Bolos para Iniciantes", "descricao": "Um curso online com t\u00e9cnicas b\u00e1sicas de decora\u00e7\u00e3o de bolos."}, {"tipo": "livro", "titulo": "Decora\u00e7\u00e3o de Bolos: Guia Completo", "descricao": "Um livro com diversas ideias e t\u00e9cnicas de decora\u00e7\u00e3o."}], "atividades_praticas": ["Prepare uma ganache de chocolate e utilize-a para cobrir um bolo.", "Pratique a utiliza\u00e7\u00e3o de um bico de confeitar para criar decora\u00e7\u00f5es simples."]}], "projeto_final": "Prepare um bolo de chocolate completo, incluindo a massa, o recheio e a cobertura de sua escolha. Decore o bolo de forma criativa e apresente-o para amigos e familiares.", "recursos_complementares": ["Club House - Tudo sobre bolos: https://www.clubhouse.com.br/tudo-sobre-bolos/", "7 receitas de bolo de chocolate deliciosas e f\u00e1ceis de fazer: https://receitas.globo.com/tudo-sobre/bolo-de-chocolate/"]}','2025-10-22 19:09:39.073441','2025-10-22 19:09:39.073441',1,3);
INSERT INTO "api_gemini_trilhacurso" VALUES(4,'Dominando o Mortal: Uma Trilha Progressiva para Iniciantes','Esta trilha de aprendizado foi projetada para guiá-lo, um estudante de computação do Mackenzie, desde os fundamentos da ginástica até a execução segura e consistente de um mortal. Levando em conta sua familiaridade com resolução de problemas e pensamento lógico, aplicaremos uma abordagem estruturada e analítica para o aprendizado de novas habilidades físicas. O objetivo é que você aprenda a executar um mortal com confiança, minimizando o risco de lesões e maximizando o prazer no processo.','quero aprender a dar mortal sem cair 
','{"titulo": "Dominando o Mortal: Uma Trilha Progressiva para Iniciantes", "descricao": "Esta trilha de aprendizado foi projetada para gui\u00e1-lo, um estudante de computa\u00e7\u00e3o do Mackenzie, desde os fundamentos da gin\u00e1stica at\u00e9 a execu\u00e7\u00e3o segura e consistente de um mortal. Levando em conta sua familiaridade com resolu\u00e7\u00e3o de problemas e pensamento l\u00f3gico, aplicaremos uma abordagem estruturada e anal\u00edtica para o aprendizado de novas habilidades f\u00edsicas. O objetivo \u00e9 que voc\u00ea aprenda a executar um mortal com confian\u00e7a, minimizando o risco de les\u00f5es e maximizando o prazer no processo.", "nivel": "Iniciante", "duracao_total": "12 semanas", "modulos": [{"numero": 1, "titulo": "Prepara\u00e7\u00e3o F\u00edsica e Flexibilidade", "descricao": "Este m\u00f3dulo foca em construir a base f\u00edsica necess\u00e1ria para realizar um mortal com seguran\u00e7a. A flexibilidade, for\u00e7a e consci\u00eancia corporal s\u00e3o essenciais para progredir nos pr\u00f3ximos m\u00f3dulos.", "duracao": "2 semanas", "topicos": ["Aquecimento Din\u00e2mico: Alongamentos ativos para preparar os m\u00fasculos.", "Alongamento Est\u00e1tico: Melhorando a flexibilidade geral e a amplitude de movimento.", "Fortalecimento do Core: Exerc\u00edcios para fortalecer o abd\u00f4men e a regi\u00e3o lombar.", "Condicionamento Card\u00edaco: Aumentando a resist\u00eancia para treinos mais longos e eficazes.", "Mobilidade Articular: Exerc\u00edcios para melhorar a mobilidade dos ombros, quadris e tornozelos."], "recursos": [{"tipo": "video", "titulo": "Alongamentos Din\u00e2micos para Ginastas", "descricao": "V\u00eddeo demonstrando uma rotina completa de alongamentos din\u00e2micos."}, {"tipo": "artigo", "titulo": "A Import\u00e2ncia do Fortalecimento do Core para Ginastas", "descricao": "Artigo detalhando os benef\u00edcios e exerc\u00edcios eficazes para o fortalecimento do core."}, {"tipo": "video", "titulo": "Exerc\u00edcios de Mobilidade para Gin\u00e1stica", "descricao": "V\u00eddeo demonstrando exerc\u00edcios para melhorar a mobilidade em \u00e1reas chave para a gin\u00e1stica."}], "atividades_praticas": ["Realizar uma rotina di\u00e1ria de aquecimento din\u00e2mico e alongamento est\u00e1tico (15-20 minutos).", "Executar exerc\u00edcios de fortalecimento do core 3 vezes por semana (prancha, abdominais, superman).", "Praticar exerc\u00edcios de mobilidade articular (rota\u00e7\u00f5es de ombro, c\u00edrculos de quadril, flex\u00f5es de tornozelo) diariamente."]}, {"numero": 2, "titulo": "Fundamentos da Gin\u00e1stica e Consci\u00eancia Corporal", "descricao": "Neste m\u00f3dulo, voc\u00ea aprender\u00e1 os movimentos b\u00e1sicos da gin\u00e1stica que s\u00e3o pr\u00e9-requisitos para o mortal. Desenvolver\u00e1 uma melhor consci\u00eancia do seu corpo no espa\u00e7o e a capacidade de controlar seus movimentos.", "duracao": "2 semanas", "topicos": ["Rolamentos: Para frente e para tr\u00e1s, dominando a t\u00e9cnica correta.", "Parada de M\u00e3os: Construindo for\u00e7a e equil\u00edbrio na posi\u00e7\u00e3o invertida.", "Roda: Aperfei\u00e7oando a t\u00e9cnica e a coordena\u00e7\u00e3o.", "Ponte: Melhorando a flexibilidade da coluna e a for\u00e7a dos ombros.", "Saltos: Dominando diferentes tipos de saltos (tesoura, grupado, carpado) em um mini-trampolim."], "recursos": [{"tipo": "video", "titulo": "Tutorial de Rolamento para Frente e para Tr\u00e1s", "descricao": "V\u00eddeo instrutivo mostrando a t\u00e9cnica correta para rolamentos seguros e eficazes."}, {"tipo": "video", "titulo": "Como Aprender a Parada de M\u00e3os: Guia Passo a Passo", "descricao": "V\u00eddeo detalhado com progress\u00f5es para aprender a parada de m\u00e3os."}, {"tipo": "video", "titulo": "Aprenda a Roda Perfeita", "descricao": "V\u00eddeo com dicas e exerc\u00edcios para aperfei\u00e7oar a roda."}], "atividades_praticas": ["Praticar rolamentos para frente e para tr\u00e1s diariamente, focando na t\u00e9cnica correta.", "Treinar a parada de m\u00e3os contra a parede (3 s\u00e9ries de 30 segundos).", "Praticar a roda em um espa\u00e7o seguro e com a supervis\u00e3o de algu\u00e9m experiente (se poss\u00edvel).", "Realizar exerc\u00edcios para fortalecer a ponte (3 s\u00e9ries de 10 repeti\u00e7\u00f5es)."]}, {"numero": 3, "titulo": "A Roda Sem M\u00e3os (Round-off) e o Salto Mortal \u00e0 Frente (Tuck)", "descricao": "Este m\u00f3dulo introduz a roda sem m\u00e3os (round-off), um movimento crucial para gerar a energia necess\u00e1ria para o mortal. Tamb\u00e9m come\u00e7aremos a praticar o tuck, a forma b\u00e1sica do salto mortal \u00e0 frente.", "duracao": "4 semanas", "topicos": ["Roda Sem M\u00e3os (Round-off): Aprendendo a t\u00e9cnica correta e a gerar impulso.", "Mini-Trampolim: Introdu\u00e7\u00e3o ao salto mortal \u00e0 frente (tuck) no mini-trampolim.", "Progress\u00f5es de Salto Mortal: Usando colch\u00f5es e equipamentos de seguran\u00e7a para praticar o salto mortal.", "Aterrissagem: Praticando a aterrissagem correta para evitar les\u00f5es.", "V\u00eddeos Anal\u00edticos: An\u00e1lise da biomec\u00e2nica do round-off e do tuck."], "recursos": [{"tipo": "video", "titulo": "Tutorial de Round-off Passo a Passo", "descricao": "V\u00eddeo detalhado com exerc\u00edcios e dicas para aprender o round-off."}, {"tipo": "video", "titulo": "Aprenda o Salto Mortal \u00e0 Frente (Tuck) no Mini-Trampolim", "descricao": "V\u00eddeo instrutivo mostrando as progress\u00f5es para aprender o tuck no mini-trampolim."}, {"tipo": "artigo", "titulo": "A Biomec\u00e2nica do Salto Mortal", "descricao": "Artigo cient\u00edfico analisando a biomec\u00e2nica do salto mortal."}], "atividades_praticas": ["Praticar o round-off diariamente, focando na t\u00e9cnica e no impulso.", "Treinar o tuck no mini-trampolim (3 s\u00e9ries de 10 repeti\u00e7\u00f5es).", "Utilizar colch\u00f5es e equipamentos de seguran\u00e7a para praticar o salto mortal em progress\u00f5es menores.", "Gravar v\u00eddeos dos seus treinos para analisar a t\u00e9cnica e identificar \u00e1reas para melhoria (aplicando seus conhecimentos de computa\u00e7\u00e3o para processamento e an\u00e1lise de v\u00eddeo, se desejar)."]}, {"numero": 4, "titulo": "Aperfei\u00e7oando o Mortal e Aterrissagem Segura", "descricao": "Neste m\u00f3dulo final, voc\u00ea se concentrar\u00e1 em aperfei\u00e7oar a t\u00e9cnica do mortal, aumentar a confian\u00e7a e a consist\u00eancia, e garantir uma aterrissagem segura.", "duracao": "4 semanas", "topicos": ["Mortal Completo: Praticando o mortal completo com seguran\u00e7a e supervis\u00e3o.", "Corre\u00e7\u00f5es T\u00e9cnicas: Identificando e corrigindo erros comuns na t\u00e9cnica.", "Aterrissagem: Aperfei\u00e7oando a aterrissagem para minimizar o impacto e prevenir les\u00f5es.", "Mentalidade: Desenvolvendo a confian\u00e7a e a concentra\u00e7\u00e3o necess\u00e1rias para executar o mortal com sucesso.", "Estrat\u00e9gias de Visualiza\u00e7\u00e3o: Utilizando t\u00e9cnicas de visualiza\u00e7\u00e3o para melhorar a performance."], "recursos": [{"tipo": "video", "titulo": "Dicas para um Salto Mortal Perfeito", "descricao": "V\u00eddeo com dicas avan\u00e7adas para aperfei\u00e7oar a t\u00e9cnica do salto mortal."}, {"tipo": "artigo", "titulo": "Psicologia do Esporte: A Import\u00e2ncia da Confian\u00e7a na Gin\u00e1stica", "descricao": "Artigo explorando o papel da confian\u00e7a e da mentalidade no desempenho da gin\u00e1stica."}, {"tipo": "video", "titulo": "Progress\u00f5es para Aterrissagem Segura no Salto Mortal", "descricao": "V\u00eddeo demonstrando exerc\u00edcios e t\u00e9cnicas para aperfei\u00e7oar a aterrissagem."}], "atividades_praticas": ["Praticar o mortal completo com a supervis\u00e3o de um treinador experiente ou em um ambiente seguro com equipamentos de prote\u00e7\u00e3o.", "Gravar v\u00eddeos dos seus treinos e analisar a t\u00e9cnica com um treinador ou colega.", "Praticar exerc\u00edcios de aterrissagem para fortalecer os m\u00fasculos e melhorar a estabilidade.", "Utilizar t\u00e9cnicas de visualiza\u00e7\u00e3o para imaginar a execu\u00e7\u00e3o perfeita do mortal antes de praticar."]}], "projeto_final": "Gravar um v\u00eddeo de alta qualidade mostrando voc\u00ea executando o mortal de forma segura e consistente. Analise o v\u00eddeo usando suas habilidades de computa\u00e7\u00e3o para identificar pontos fortes e \u00e1reas que precisam de melhoria. Compartilhe o v\u00eddeo com outros aprendizes e pe\u00e7a feedback construtivo.", "recursos_complementares": ["Encontre um treinador de gin\u00e1stica qualificado para orienta\u00e7\u00e3o personalizada.", "Assista a v\u00eddeos de ginastas profissionais para inspira\u00e7\u00e3o e aprendizado.", "Participe de f\u00f3runs online e comunidades de gin\u00e1stica para trocar experi\u00eancias e obter suporte.", "Utilize aplicativos de an\u00e1lise de movimento para monitorar seu progresso (aplicando seus conhecimentos de computa\u00e7\u00e3o para avaliar a precis\u00e3o e aplicabilidade dos dados gerados).", "Priorize sempre a seguran\u00e7a e n\u00e3o hesite em pedir ajuda quando necess\u00e1rio."]}','2025-10-22 19:11:32.534071','2025-10-22 19:11:32.534071',1,1);
CREATE TABLE "api_trilha" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(200) NOT NULL, "descricao" text NOT NULL, "conteudo" text NOT NULL, "ativa" bool NOT NULL, "data_criacao" datetime NOT NULL, "data_atualizacao" datetime NOT NULL, "area_id" bigint NULL REFERENCES "api_area" ("id") DEFERRABLE INITIALLY DEFERRED, "usuario_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "api_trilha" VALUES(2,'Trabalhando deitado: Ergonomia, Produtividade e Bem-Estar','Esta trilha de aprendizado visa fornecer o conhecimento e as ferramentas necessárias para criar um ambiente de trabalho confortável e produtivo em posições reclinadas, minimizando riscos à saúde e maximizando o bem-estar.','{
  "titulo": "Trabalhando deitado: Ergonomia, Produtividade e Bem-Estar",
  "descricao": "Esta trilha de aprendizado visa fornecer o conhecimento e as ferramentas necessárias para criar um ambiente de trabalho confortável e produtivo em posições reclinadas, minimizando riscos à saúde e maximizando o bem-estar.",
  "nivel": "Iniciante",
  "duracao_total": "4 semanas",
  "modulos": [
    {
      "numero": 1,
      "titulo": "Fundamentos da Ergonomia Reclinada",
      "descricao": "Compreender os princípios básicos da ergonomia e como adaptá-los para posições de trabalho reclinadas.",
      "duracao": "1 semana",
      "topicos": [
        "Introdução à Ergonomia: Postura, Repetição e Força",
        "Anatomia da Coluna Vertebral e Impacto da Postura",
        "Riscos de Longas Jornadas de Trabalho em Posturas Sedentárias",
        "Princípios da Ergonomia Reclinada: Ângulos, Suporte e Alinhamento",
        "Benefícios e Limitações do Trabalho Deitado"
      ],
      "recursos": [
        {
          "tipo": "artigo",
          "titulo": "Ergonomics for Dummies",
          "descricao": "Uma introdução acessível aos princípios da ergonomia."
        },
        {
          "tipo": "video",
          "titulo": "The Importance of Ergonomics in the Workplace",
          "descricao": "Vídeo explicando a importância da ergonomia para a saúde e produtividade."
        },
        {
          "tipo": "artigo",
          "titulo": "Positioning the Laptop for the Best Ergonomic Setup",
          "descricao": "Artigo sobre posicionamento ergonômico de notebooks."
        }
      ],
      "atividades_praticas": [
        "Avalie sua postura atual ao trabalhar sentado e identifique áreas de tensão.",
        "Pesquise e compare diferentes tipos de cadeiras reclináveis e camas ajustáveis."
      ]
    },
    {
      "numero": 2,
      "titulo": "Equipamentos e Acessórios Essenciais",
      "descricao": "Conhecer os equipamentos e acessórios necessários para montar um espaço de trabalho ergonômico em posições reclinadas.",
      "duracao": "1 semana",
      "topicos": [
        "Cadeiras Reclináveis Ergonômicas: Tipos, Ajustes e Recursos",
        "Camas Ajustáveis: Mecanismos, Níveis de Inclinação e Conforto",
        "Suportes para Notebook e Tablet: Posicionamento Ideal e Estabilidade",
        "Teclados e Mouses Ergonômicos: Design, Funcionalidade e Prevenção de LER/DORT",
        "Iluminação Adequada: Luminosidade, Temperatura de Cor e Redução de Reflexos"
      ],
      "recursos": [
        {
          "tipo": "video",
          "titulo": "Best Ergonomic Office Chairs 2023",
          "descricao": "Review de cadeiras ergonômicas."
        },
        {
          "tipo": "artigo",
          "titulo": "Choosing the Right Ergonomic Keyboard",
          "descricao": "Guia para escolher o teclado ergonômico ideal."
        },
        {
          "tipo": "artigo",
          "titulo": "Laptop Stands: Are They Worth It?",
          "descricao": "Artigo analisando a importância dos suportes de laptop."
        }
      ],
      "atividades_praticas": [
        "Visite uma loja de móveis e experimente diferentes cadeiras reclináveis e camas ajustáveis.",
        "Pesquise e compare preços de suportes para notebook e tablets ergonômicos online.",
        "Teste diferentes teclados e mouses ergonômicos para encontrar o que melhor se adapta à sua mão."
      ]
    },
    {
      "numero": 3,
      "titulo": "Técnicas de Postura e Movimento",
      "descricao": "Aprender técnicas de postura correta e exercícios para prevenir dores e lesões ao trabalhar deitado.",
      "duracao": "1 semana",
      "topicos": [
        "Alinhamento da Coluna Vertebral em Posições Reclinadas",
        "Suporte Lombar e Cervical Adequado",
        "Micro Pausas: Alongamentos e Exercícios Simples para Relaxar os Músculos",
        "Exercícios de Fortalecimento para a Coluna e o Core",
        "Técnicas de Respiração para Reduzir o Estresse e a Tensão"
      ],
      "recursos": [
        {
          "tipo": "video",
          "titulo": "Stretches You Can Do While Lying in Bed",
          "descricao": "Vídeos de alongamentos que podem ser feitos na cama."
        },
        {
          "tipo": "artigo",
          "titulo": "5 Simple Exercises for a Healthy Spine",
          "descricao": "Artigo com exercícios para a saúde da coluna."
        },
        {
          "tipo": "video",
          "titulo": "Deep Breathing Exercises for Stress Relief",
          "descricao": "Vídeo com exercícios de respiração para alívio do estresse."
        }
      ],
      "atividades_praticas": [
        "Pratique alongamentos leves a cada 20-30 minutos enquanto trabalha deitado.",
        "Incorpore exercícios de fortalecimento para o core em sua rotina diária.",
        "Reserve alguns minutos por dia para praticar técnicas de respiração."
      ]
    },
    {
      "numero": 4,
      "titulo": "Otimização do Ambiente e da Produtividade",
      "descricao": "Aprender a otimizar o ambiente de trabalho e a produtividade ao trabalhar deitado.",
      "duracao": "1 semana",
      "topicos": [
        "Organização do Espaço de Trabalho: Acesso Fácil a Ferramentas e Materiais",
        "Gerenciamento do Tempo: Técnicas de Pomodoro e Blocos de Tempo",
        "Comunicação e Colaboração Remota: Ferramentas e Estratégias Eficazes",
        "Saúde Mental e Bem-Estar: Mindfulness e Autocuidado",
        "Adaptação e Flexibilidade: Ajustando o Ambiente e a Rotina às Suas Necessidades"
      ],
      "recursos": [
        {
          "tipo": "artigo",
          "titulo": "Time Management Techniques That Work",
          "descricao": "Artigo com diversas técnicas de gerenciamento de tempo."
        },
        {
          "tipo": "video",
          "titulo": "Mindfulness for Beginners",
          "descricao": "Introdução ao mindfulness."
        },
        {
          "tipo": "artigo",
          "titulo": "Remote Collaboration Tools and Strategies",
          "descricao": "Artigo sobre ferramentas e estratégias para colaboração remota."
        }
      ],
      "atividades_praticas": [
        "Organize seu espaço de trabalho de forma a ter fácil acesso a tudo o que precisa.",
        "Experimente diferentes técnicas de gerenciamento de tempo para encontrar a que melhor se adapta a você.",
        "Incorpore práticas de mindfulness em sua rotina diária."
      ]
    }
  ],
  "projeto_final": "Monte um espaço de trabalho ergonômico e funcional para trabalhar deitado, levando em consideração os princípios da ergonomia, os equipamentos e acessórios adequados, as técnicas de postura e movimento, e a otimização do ambiente e da produtividade. Documente o processo com fotos e compartilhe suas experiências e resultados.",
  "recursos_complementares": [
    "Livro: ''Ergonomics: Work-Related Musculoskeletal Disorders'' de Steven Lavender",
    "Site: The Ergonomics Center of North Carolina (www.ergo.ncsu.edu)"
  ]
}',1,'2025-11-16 03:56:48.839344','2025-11-16 04:13:24.087478',1,2);
INSERT INTO "api_trilha" VALUES(3,'Fundamentos do Pensamento Crítico e Tomada de Decisão Consciente','Esta trilha de aprendizado tem como objetivo capacitar o indivíduo a desenvolver habilidades de pensamento crítico, reconhecer padrões de manipulação e tomar decisões mais informadas e conscientes em diferentes aspectos da vida.','{
  "titulo": "Fundamentos do Pensamento Crítico e Tomada de Decisão Consciente",
  "descricao": "Esta trilha de aprendizado tem como objetivo capacitar o indivíduo a desenvolver habilidades de pensamento crítico, reconhecer padrões de manipulação e tomar decisões mais informadas e conscientes em diferentes aspectos da vida.",
  "nivel": "Iniciante",
  "duracao_total": "8 semanas",
  "modulos": [
    {
      "numero": 1,
      "titulo": "Introdução ao Pensamento Crítico",
      "descricao": "Compreender os conceitos básicos do pensamento crítico e sua importância na vida cotidiana.",
      "duracao": "1 semana",
      "topicos": [
        "O que é pensamento crítico e por que é importante?",
        "Viés cognitivos comuns e como eles afetam o julgamento",
        "Identificando informações confiáveis e fontes duvidosas"
      ],
      "recursos": [
        {
          "tipo": "artigo",
          "titulo": "A Beginner''s Guide to Critical Thinking and Strategic Planning",
          "descricao": "Artigo que explora os fundamentos do pensamento crítico."
        },
        {
          "tipo": "video",
          "titulo": "Introdução ao Pensamento Crítico",
          "descricao": "Vídeo explicativo sobre o que é pensamento crítico."
        }
      ],
      "atividades_praticas": [
        "Analise de notícias e identificação de possíveis vieses.",
        "Discussão em grupo sobre dilemas éticos."
      ]
    },
    {
      "numero": 2,
      "titulo": "Lógica e Argumentação",
      "descricao": "Aprender os princípios da lógica formal e informal, e como construir e avaliar argumentos sólidos.",
      "duracao": "2 semanas",
      "topicos": [
        "Princípios básicos da lógica (dedução, indução, abdução)",
        "Falácias lógicas comuns e como identificá-las",
        "Construindo argumentos persuasivos e racionais"
      ],
      "recursos": [
        {
          "tipo": "livro",
          "titulo": "Lógica Informal",
          "descricao": "Livro sobre os princípios da lógica informal e identificação de falácias."
        },
        {
          "tipo": "curso",
          "titulo": "Critical Thinking: Learn to Think Critically",
          "descricao": "Curso online sobre pensamento crítico e lógica."
        }
      ],
      "atividades_praticas": [
        "Análise de discursos políticos e identificação de falácias.",
        "Debates simulados sobre temas controversos."
      ]
    },
    {
      "numero": 3,
      "titulo": "Reconhecendo Padrões de Manipulação",
      "descricao": "Identificar e analisar técnicas de persuasão e manipulação utilizadas em diferentes contextos.",
      "duracao": "2 semanas",
      "topicos": [
        "Técnicas de persuasão (gatilhos mentais, storytelling)",
        "Propaganda e desinformação",
        "Manipulação emocional"
      ],
      "recursos": [
        {
          "tipo": "artigo",
          "titulo": "The Psychology of Persuasion",
          "descricao": "Artigo sobre as técnicas psicológicas de persuasão."
        },
        {
          "tipo": "video",
          "titulo": "Como identificar notícias falsas",
          "descricao": "Vídeo sobre identificação de notícias falsas e desinformação."
        }
      ],
      "atividades_praticas": [
        "Análise de anúncios publicitários e identificação de técnicas de persuasão.",
        "Discussão sobre casos de manipulação em mídias sociais."
      ]
    },
    {
      "numero": 4,
      "titulo": "Tomada de Decisão Consciente",
      "descricao": "Desenvolver habilidades para tomar decisões mais informadas e conscientes, considerando diferentes perspectivas e consequências.",
      "duracao": "2 semanas",
      "topicos": [
        "Modelos de tomada de decisão (racional, intuitivo)",
        "Análise de risco e benefícios",
        "A importância da inteligência emocional na tomada de decisão"
      ],
      "recursos": [
        {
          "tipo": "livro",
          "titulo": "Thinking, Fast and Slow",
          "descricao": "Livro sobre os dois sistemas de pensamento e como eles influenciam a tomada de decisão."
        },
        {
          "tipo": "curso",
          "titulo": "Decision-Making Skills",
          "descricao": "Curso online sobre habilidades de tomada de decisão."
        }
      ],
      "atividades_praticas": [
        "Estudos de caso de decisões complexas.",
        "Simulação de situações de tomada de decisão sob pressão."
      ]
    },
    {
      "numero": 5,
      "titulo": "Aplicando o Pensamento Crítico na Prática",
      "descricao": "Aplicar as habilidades aprendidas em diferentes contextos, como finanças pessoais, saúde e relacionamentos.",
      "duracao": "1 semana",
      "topicos": [
        "Pensamento crítico e finanças pessoais (investimentos, dívidas)",
        "Pensamento crítico e saúde (informações médicas, tratamentos)",
        "Pensamento crítico e relacionamentos (comunicação, resolução de conflitos)"
      ],
      "recursos": [
        {
          "tipo": "artigo",
          "titulo": "Critical Thinking in Everyday Life",
          "descricao": "Artigo sobre a aplicação do pensamento crítico na vida cotidiana."
        },
        {
          "tipo": "video",
          "titulo": "Como usar o pensamento crítico para melhorar sua vida",
          "descricao": "Vídeo sobre como aplicar o pensamento crítico em diferentes áreas da vida."
        }
      ],
      "atividades_praticas": [
        "Análise de um plano financeiro pessoal.",
        "Discussão sobre a importância do pensamento crítico na escolha de um plano de saúde."
      ]
    }
  ],
  "projeto_final": "Elaborar um plano de ação para aplicar o pensamento crítico em uma área específica da sua vida, identificando desafios e oportunidades.",
  "recursos_complementares": [
    "The Skeptic''s Guide to the Universe (podcast)",
    "FactCheck.org (site de checagem de fatos)"
  ]
}',1,'2025-11-16 05:24:08.336228','2025-11-16 05:24:08.336228',1,2);
INSERT INTO "api_trilha" VALUES(4,'Fundamentos da Eletrônica para Iniciantes','Esta trilha de aprendizado foi projetada para fornecer uma base sólida em eletrônica, abordando desde os conceitos básicos até a construção de circuitos simples. O objetivo é capacitar o aluno a entender o funcionamento de componentes eletrônicos, circuitos e a realizar projetos práticos.','{
  "titulo": "Fundamentos da Eletrônica para Iniciantes",
  "descricao": "Esta trilha de aprendizado foi projetada para fornecer uma base sólida em eletrônica, abordando desde os conceitos básicos até a construção de circuitos simples. O objetivo é capacitar o aluno a entender o funcionamento de componentes eletrônicos, circuitos e a realizar projetos práticos.",
  "nivel": "Iniciante",
  "duracao_total": "8 semanas",
  "modulos": [
    {
      "numero": 1,
      "titulo": "Introdução à Eletrônica e Grandezas Elétricas",
      "descricao": "Este módulo aborda os conceitos fundamentais da eletrônica, incluindo a natureza da eletricidade, grandezas elétricas como tensão, corrente e resistência, além da Lei de Ohm.",
      "duracao": "1 semana",
      "topicos": [
        "O que é eletrônica e suas aplicações",
        "Átomo e a natureza da eletricidade",
        "Tensão (Voltagem): Conceito e unidade de medida (Volt)",
        "Corrente Elétrica: Conceito e unidade de medida (Ampère)",
        "Resistência Elétrica: Conceito e unidade de medida (Ohm)",
        "Lei de Ohm: Relação entre tensão, corrente e resistência",
        "Potência Elétrica: Conceito e unidade de medida (Watt)",
        "Tipos de corrente elétrica: Contínua (DC) e Alternada (AC)"
      ],
      "recursos": [
        {
          "tipo": "video",
          "titulo": "Eletrônica para Iniciantes - Curso Completo",
          "descricao": "Vídeo introdutório sobre os conceitos básicos da eletrônica."
        },
        {
          "tipo": "livro",
          "titulo": "Eletrônica para Leigos",
          "descricao": "Capítulos iniciais sobre eletricidade e grandezas elétricas."
        },
        {
          "tipo": "artigo",
          "titulo": "Lei de Ohm - Brasil Escola",
          "descricao": "Artigo detalhado sobre a Lei de Ohm e suas aplicações."
        }
      ],
      "atividades_praticas": [
        "Medição de tensão, corrente e resistência em circuitos simples usando um multímetro.",
        "Cálculo da corrente em um circuito utilizando a Lei de Ohm.",
        "Montagem de um circuito com resistores em série e paralelo e medição da resistência equivalente."
      ]
    },
    {
      "numero": 2,
      "titulo": "Componentes Eletrônicos Passivos",
      "descricao": "Este módulo explora os componentes passivos mais comuns, como resistores, capacitores e indutores, suas características, aplicações e como identificá-los.",
      "duracao": "2 semanas",
      "topicos": [
        "Resistores: Tipos, código de cores, valores e tolerância.",
        "Capacitores: Tipos (eletrolíticos, cerâmicos, etc.), capacitância, tensão de trabalho e aplicações.",
        "Indutores: Tipos, indutância, reatância indutiva e aplicações.",
        "Associação de resistores, capacitores e indutores (série e paralelo).",
        "Leitura de datasheet de componentes passivos"
      ],
      "recursos": [
        {
          "tipo": "video",
          "titulo": "Resistores - Mundo da Elétrica",
          "descricao": "Vídeo explicando o funcionamento e o código de cores dos resistores."
        },
        {
          "tipo": "artigo",
          "titulo": "Capacitores: O que são, como funcionam, tipos e aplicações - Embarcados",
          "descricao": "Artigo completo sobre capacitores."
        },
        {
          "tipo": "livro",
          "titulo": "Eletrônica: Volume 1 - Boylestad",
          "descricao": "Capítulo sobre componentes passivos."
        }
      ],
      "atividades_praticas": [
        "Identificação de resistores através do código de cores e medição com multímetro.",
        "Medição da capacitância de diferentes tipos de capacitores.",
        "Montagem de filtros RC passa-baixa e passa-alta em protoboard e medição da resposta em frequência com gerador de sinais e osciloscópio (opcional).",
        "Construir um divisor de tensão utilizando resistores e medir as tensões resultantes."
      ]
    },
    {
      "numero": 3,
      "titulo": "Componentes Eletrônicos Ativos",
      "descricao": "Este módulo apresenta os componentes ativos mais utilizados, como diodos e transistores, seus princípios de funcionamento e aplicações em circuitos básicos.",
      "duracao": "2 semanas",
      "topicos": [
        "Diodos: Tipos (retificador, LED, Zener), polarização direta e reversa, aplicações.",
        "Transistores Bipolares (BJT): NPN e PNP, regiões de operação (corte, ativa, saturação), aplicações como chave e amplificador.",
        "Transistores de Efeito de Campo (FET): MOSFET, JFET, princípios de funcionamento e aplicações.",
        "Leitura de datasheet de componentes ativos"
      ],
      "recursos": [
        {
          "tipo": "video",
          "titulo": "Diodos: O que são e como funcionam - FilipeFlop",
          "descricao": "Vídeo explicativo sobre diodos."
        },
        {
          "tipo": "artigo",
          "titulo": "Transistores: Tipos e como funcionam - WR Kits",
          "descricao": "Artigo sobre transistores e suas aplicações."
        },
        {
          "tipo": "curso",
          "titulo": "Curso de Eletrônica Analógica - Udemy (seções relevantes)",
          "descricao": "Seções introdutórias sobre diodos e transistores."
        }
      ],
      "atividades_praticas": [
        "Montagem de um circuito retificador de meia onda e onda completa com diodos.",
        "Construção de um circuito chaveador utilizando um transistor BJT.",
        "Acionamento de um LED com um transistor.",
        "Teste de diodos e transistores com multímetro."
      ]
    },
    {
      "numero": 4,
      "titulo": "Circuitos Eletrônicos Básicos e Protoboard",
      "descricao": "Este módulo foca na montagem de circuitos em protoboard, utilizando os componentes aprendidos nos módulos anteriores, e na análise de circuitos simples.",
      "duracao": "2 semanas",
      "topicos": [
        "Protoboard: Estrutura, funcionamento e boas práticas de montagem.",
        "Fontes de alimentação: Criação de fontes reguladas simples.",
        "Amplificadores operacionais (Op-Amps): Introdução e aplicações básicas (amplificador inversor, não inversor, seguidor de tensão).",
        "Circuitos com sensores: Utilização de sensores de luz (LDR) e temperatura (termistores).",
        "Leitura de esquemas elétricos básicos."
      ],
      "recursos": [
        {
          "tipo": "video",
          "titulo": "Como usar Protoboard - WR Kits",
          "descricao": "Vídeo tutorial sobre como usar a protoboard."
        },
        {
          "tipo": "artigo",
          "titulo": "Amplificadores Operacionais: Introdução - Embarcados",
          "descricao": "Artigo introdutório sobre amplificadores operacionais."
        },
        {
          "tipo": "curso",
          "titulo": "Eletrônica Básica para Makers - Cursera (seções relevantes)",
          "descricao": "Seções sobre protoboard e circuitos básicos."
        }
      ],
      "atividades_praticas": [
        "Montagem de um amplificador inversor com um amplificador operacional.",
        "Criação de um circuito sensor de luz utilizando um LDR e um transistor.",
        "Montagem de uma fonte de alimentação regulada simples com um regulador de tensão.",
        "Construção de um circuito comparador utilizando um amplificador operacional."
      ]
    },
    {
      "numero": 5,
      "titulo": "Ferramentas e Instrumentação",
      "descricao": "Este módulo apresenta as ferramentas e instrumentos essenciais para trabalhar com eletrônica, incluindo multímetro, osciloscópio, gerador de funções e ferro de solda.",
      "duracao": "1 semana",
      "topicos": [
        "Multímetro: Medição de tensão, corrente, resistência e continuidade.",
        "Osciloscópio: Visualização de sinais elétricos e medição de frequência e amplitude.",
        "Gerador de funções: Geração de sinais senoidais, quadrados e triangulares.",
        "Ferro de solda: Técnicas de soldagem e dessoldagem.",
        "Ferramentas manuais: Alicates, chaves de fenda, etc."
      ],
      "recursos": [
        {
          "tipo": "video",
          "titulo": "Como usar o Multímetro - Mundo da Elétrica",
          "descricao": "Tutorial sobre como usar um multímetro."
        },
        {
          "tipo": "artigo",
          "titulo": "Osciloscópio: O que é e como usar - Newton C. Braga",
          "descricao": "Artigo sobre o funcionamento e utilização do osciloscópio."
        },
        {
          "tipo": "video",
          "titulo": "Técnicas de Soldagem - FilipeFlop",
          "descricao": "Vídeo sobre técnicas de soldagem."
        }
      ],
      "atividades_praticas": [
        "Medição de tensão, corrente e resistência em diferentes circuitos com um multímetro.",
        "Visualização de sinais elétricos com um osciloscópio.",
        "Soldagem e dessoldagem de componentes em uma placa de circuito impresso.",
        "Gerar diferentes formas de onda com um gerador de funções."
      ]
    }
  ],
  "projeto_final": "Construção de um semáforo simples com LEDs, resistores, um CI 555 (timer) e uma protoboard. O projeto deve envolver a montagem do circuito, o cálculo dos valores dos componentes e a análise do funcionamento.",
  "recursos_complementares": [
    "Datasheets de componentes eletrônicos (disponíveis online)",
    "Simuladores de circuitos eletrônicos (e.g., Tinkercad, EveryCircuit)",
    "Fóruns e comunidades online de eletrônica (e.g., Reddit - r/electronics)"
  ]
}',0,'2025-11-16 05:31:02.593598','2025-11-16 05:31:08.207525',2,2);
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO "auth_permission" VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES(5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES(6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES(8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES(9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES(10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES(11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES(12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES(13,4,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES(14,4,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES(15,4,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES(16,4,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES(17,5,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES(18,5,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES(19,5,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES(20,5,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES(21,6,'add_usuario','Can add user');
INSERT INTO "auth_permission" VALUES(22,6,'change_usuario','Can change user');
INSERT INTO "auth_permission" VALUES(23,6,'delete_usuario','Can delete user');
INSERT INTO "auth_permission" VALUES(24,6,'view_usuario','Can view user');
INSERT INTO "auth_permission" VALUES(25,7,'add_trilhacurso','Can add Trilha de Curso');
INSERT INTO "auth_permission" VALUES(26,7,'change_trilhacurso','Can change Trilha de Curso');
INSERT INTO "auth_permission" VALUES(27,7,'delete_trilhacurso','Can delete Trilha de Curso');
INSERT INTO "auth_permission" VALUES(28,7,'view_trilhacurso','Can view Trilha de Curso');
INSERT INTO "auth_permission" VALUES(29,8,'add_trilha','Can add Trilha');
INSERT INTO "auth_permission" VALUES(30,8,'change_trilha','Can change Trilha');
INSERT INTO "auth_permission" VALUES(31,8,'delete_trilha','Can delete Trilha');
INSERT INTO "auth_permission" VALUES(32,8,'view_trilha','Can view Trilha');
INSERT INTO "auth_permission" VALUES(33,9,'add_area','Can add Área');
INSERT INTO "auth_permission" VALUES(34,9,'change_area','Can change Área');
INSERT INTO "auth_permission" VALUES(35,9,'delete_area','Can delete Área');
INSERT INTO "auth_permission" VALUES(36,9,'view_area','Can view Área');
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
INSERT INTO "django_admin_log" VALUES(1,'1','Python para iniciantes - admin',1,'[{"added": {}}]',7,2,'2025-09-22 21:54:53.778896');
INSERT INTO "django_admin_log" VALUES(2,'2','caue',2,'[{"changed": {"fields": ["Username"]}}]',6,2,'2025-09-22 21:57:44.007091');
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO "django_content_type" VALUES(1,'admin','logentry');
INSERT INTO "django_content_type" VALUES(2,'auth','permission');
INSERT INTO "django_content_type" VALUES(3,'auth','group');
INSERT INTO "django_content_type" VALUES(4,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(5,'sessions','session');
INSERT INTO "django_content_type" VALUES(6,'usuarios','usuario');
INSERT INTO "django_content_type" VALUES(7,'api_gemini','trilhacurso');
INSERT INTO "django_content_type" VALUES(8,'api','trilha');
INSERT INTO "django_content_type" VALUES(9,'api','area');
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2025-09-01 18:56:10.925961');
INSERT INTO "django_migrations" VALUES(2,'contenttypes','0002_remove_content_type_name','2025-09-01 18:56:11.012059');
INSERT INTO "django_migrations" VALUES(3,'auth','0001_initial','2025-09-01 18:56:11.164211');
INSERT INTO "django_migrations" VALUES(4,'auth','0002_alter_permission_name_max_length','2025-09-01 18:56:11.261549');
INSERT INTO "django_migrations" VALUES(5,'auth','0003_alter_user_email_max_length','2025-09-01 18:56:11.333590');
INSERT INTO "django_migrations" VALUES(6,'auth','0004_alter_user_username_opts','2025-09-01 18:56:11.417866');
INSERT INTO "django_migrations" VALUES(7,'auth','0005_alter_user_last_login_null','2025-09-01 18:56:11.500354');
INSERT INTO "django_migrations" VALUES(8,'auth','0006_require_contenttypes_0002','2025-09-01 18:56:11.564602');
INSERT INTO "django_migrations" VALUES(9,'auth','0007_alter_validators_add_error_messages','2025-09-01 18:56:11.641673');
INSERT INTO "django_migrations" VALUES(10,'auth','0008_alter_user_username_max_length','2025-09-01 18:56:11.726952');
INSERT INTO "django_migrations" VALUES(11,'auth','0009_alter_user_last_name_max_length','2025-09-01 18:56:11.800130');
INSERT INTO "django_migrations" VALUES(12,'auth','0010_alter_group_name_max_length','2025-09-01 18:56:11.876537');
INSERT INTO "django_migrations" VALUES(13,'auth','0011_update_proxy_permissions','2025-09-01 18:56:11.957949');
INSERT INTO "django_migrations" VALUES(14,'auth','0012_alter_user_first_name_max_length','2025-09-01 18:56:12.025275');
INSERT INTO "django_migrations" VALUES(15,'usuarios','0001_initial','2025-09-01 18:56:12.189561');
INSERT INTO "django_migrations" VALUES(16,'admin','0001_initial','2025-09-01 18:56:12.341043');
INSERT INTO "django_migrations" VALUES(17,'admin','0002_logentry_remove_auto_add','2025-09-01 18:56:12.413080');
INSERT INTO "django_migrations" VALUES(18,'admin','0003_logentry_add_action_flag_choices','2025-09-01 18:56:12.503502');
INSERT INTO "django_migrations" VALUES(19,'sessions','0001_initial','2025-09-01 18:56:12.641209');
INSERT INTO "django_migrations" VALUES(20,'api_gemini','0001_initial','2025-09-22 20:23:22.721655');
INSERT INTO "django_migrations" VALUES(21,'api','0001_initial','2025-11-16 03:22:08.801569');
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO "django_session" VALUES('w6tkdyjn9vskc4ff32v8g8fx5gnqqk14','e30:1utA7I:j0utkP0_JUDly4nrTXoKaCVRonNp64RanauZMIYIRQI','2025-09-15 19:23:00.494192');
INSERT INTO "django_session" VALUES('3qow52mjnabo8ylt18xj9zl1fk77ovju','e30:1utAKA:U7anjjIV9pWM4-2Nx0soSFFw9WXLe2olxFAri1s7Jbc','2025-09-15 19:36:18.644385');
INSERT INTO "django_session" VALUES('4vkpebz8mrs62w3ecylkgzuirm81c3hz','.eJxVjEsOwjAMBe-SNYpst1UTluw5Q-XYDi2gROpnhbg7VOoCtm9m3ssNvK3jsC02D5O6syN3-t0Sy8PKDvTO5Va91LLOU_K74g-6-GtVe14O9-9g5GX81iBk2gXBBpUb5tAhZMHQCacIplnFiCD1sSeMwDlkE4qCgGCpbd37A_15OG8:1v0oKz:6kF5YsWn_wDbqcw058AnOBPw2Mz1Vp2WI2X2P74inPA','2025-10-06 21:44:45.623583');
INSERT INTO "django_session" VALUES('iyn4rbpc0rj5oehit1nk8mlcp4b5mnf9','.eJxVjDsOwjAQBe_iGlnxNzYlfc5grXfXJIAcKU4qxN1JpBTQvpl5b5FgW8e0NV7SROIqjLj8bhnwyfUA9IB6nyXOdV2mLA9FnrTJYSZ-3U7372CENu51UIidJ9K5i8QBKFpnVV8KGojguGi9UwSXUXlPmbXriZ3xysfgbBafLwifOJo:1vBeGl:K1uZNs-HlUFv7UYY1YIuotzGjzuWd-Qp659lhXvw1Cw','2025-11-05 19:13:11.360672');
INSERT INTO "django_session" VALUES('th1xp1apvkwty6m6gq42wxnrpbbrr658','.eJxVjDsOwjAQBe_iGln-rT-U9JzBWttrHECOFCcV4u4QKQW0b2bei0Xc1ha3QUucCjszw06_W8L8oL6Dcsd-m3me-7pMie8KP-jg17nQ83K4fwcNR_vW3mVFkJKpWkJNVhsAp5S0SmjvUTivSyZnhUOAWtCGLKv1NoRSqyRk7w_HujeK:1vG20F:JcgA0OsIRDX7Ab4UjJYw2zk4P_EXrOWkhA11UNsLaTY','2025-11-17 21:22:15.229039');
INSERT INTO "django_session" VALUES('6jwv7mz3gm4abk7oix424vuamoq9cmc9','.eJxVjEEOwiAQRe_C2pAUZii4dO8ZyAwMUjU0Ke3KeHdt0oVu_3vvv1Skba1x67LEKauzMur0uzGlh7Qd5Du126zT3NZlYr0r-qBdX-csz8vh_h1U6vVb-xERAJnRAhooHHj0RUBCllwG4wZGz5LJOSGbbDAoULxF64pJidT7A-HeOEg:1vKUDd:EfKyW_IFQTvIKRtpG4RGHS3p_CqBfBrNchQ5sTloahc','2025-11-30 04:18:29.582518');
CREATE TABLE "usuarios_usuario" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "nome" varchar(100) NOT NULL, "email" varchar(254) NOT NULL UNIQUE, "universidade" varchar(255) NOT NULL, "curso" varchar(255) NOT NULL, "ano_formatura" integer NULL, "idade" integer NULL);
INSERT INTO "usuarios_usuario" VALUES(1,'pbkdf2_sha256$1000000$r5oM7LM0iElvUaDFaAjNck$/wdAD7l94XpQ7W0jqtwgUAub0b0WCg5lxNMrJ2sr0+Q=','2025-09-01 19:36:18.758042',0,'Art','','',0,1,'2025-09-01 19:22:49.354072','Artur Siquera Sudre','art@gmail.com','Mackenzie','Computação',2028,19);
INSERT INTO "usuarios_usuario" VALUES(2,'pbkdf2_sha256$1000000$4zec3xEmpjTNJBGQMl1Xl6$ADnj5azKZrPjmdXesAWip9+ymt2yqj78mwj0+EFddmM=','2025-11-16 04:18:29.554910',1,'caue','','',1,1,'2025-09-22 21:44:12','caue','c@gmail.com','mackenzie','engenharia da computação',2028,21);
INSERT INTO "usuarios_usuario" VALUES(3,'pbkdf2_sha256$1000000$l7wyQ1YsBMEV0tRApgLpg2$1Poid3ag4H/9g72ueCkaD4/YG0/b+u5OSimNogMQ/Ew=','2025-10-22 19:13:11.338774',1,'admin','','',1,1,'2025-10-22 18:28:00.867649','Administrador','admin@estudaai.com','','',NULL,NULL);
INSERT INTO "usuarios_usuario" VALUES(4,'pbkdf2_sha256$1000000$6LkH71kAYzIg7OlWV4uNAV$GkLdVMBrI7a3XPmuTGetRdf5uKd4zRqDdXlM5mEAhkQ=','2025-11-03 21:22:15.052467',0,'teste02','','',0,1,'2025-11-03 21:22:06.174386','TESTE NUMERO DOIS','teste02@teste.com','Mackenzie','Engenharia da Computação',2028,20);
CREATE TABLE "usuarios_usuario_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "usuario_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "usuarios_usuario_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "usuario_id" bigint NOT NULL REFERENCES "usuarios_usuario" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "usuarios_usuario_groups_usuario_id_group_id_4ed5b09e_uniq" ON "usuarios_usuario_groups" ("usuario_id", "group_id");
CREATE INDEX "usuarios_usuario_groups_usuario_id_7a34077f" ON "usuarios_usuario_groups" ("usuario_id");
CREATE INDEX "usuarios_usuario_groups_group_id_e77f6dcf" ON "usuarios_usuario_groups" ("group_id");
CREATE UNIQUE INDEX "usuarios_usuario_user_permissions_usuario_id_permission_id_217cadcd_uniq" ON "usuarios_usuario_user_permissions" ("usuario_id", "permission_id");
CREATE INDEX "usuarios_usuario_user_permissions_usuario_id_60aeea80" ON "usuarios_usuario_user_permissions" ("usuario_id");
CREATE INDEX "usuarios_usuario_user_permissions_permission_id_4e5c0f2f" ON "usuarios_usuario_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "api_gemini_trilhacurso_usuario_id_23b8d66c" ON "api_gemini_trilhacurso" ("usuario_id");
CREATE INDEX "api_trilha_area_id_d6bc8d7d" ON "api_trilha" ("area_id");
CREATE INDEX "api_trilha_usuario_id_6c107f9a" ON "api_trilha" ("usuario_id");
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('django_migrations',21);
INSERT INTO "sqlite_sequence" VALUES('django_content_type',9);
INSERT INTO "sqlite_sequence" VALUES('auth_permission',36);
INSERT INTO "sqlite_sequence" VALUES('auth_group',0);
INSERT INTO "sqlite_sequence" VALUES('django_admin_log',2);
INSERT INTO "sqlite_sequence" VALUES('usuarios_usuario',4);
INSERT INTO "sqlite_sequence" VALUES('api_gemini_trilhacurso',4);
INSERT INTO "sqlite_sequence" VALUES('api_area',2);
INSERT INTO "sqlite_sequence" VALUES('api_trilha',4);
COMMIT;
