# Caso de Uso – Login no Sistema EstudaAI

**Atores:**  
- Aluno  
- Administrador  

---

## Descrição

Este caso de uso descreve o processo de autenticação de um usuário (Aluno ou Administrador)
no sistema EstudaAI. Após informar credenciais válidas, o sistema direciona o usuário para
a interface correspondente ao seu perfil.

---

## Pré-condições

- O usuário possui cadastro no sistema.  
- O usuário está na tela de login.

---

## Pós-condições

- O usuário é autenticado e direcionado para:
  - Área do Aluno; ou  
  - Painel Administrativo.
- Em caso de falha, o sistema exibe mensagem de erro.
- Após tentativas excessivas falhas, a conta pode ser bloqueada temporariamente.

---

## Fluxo principal

1. O usuário acessa a tela de login.
2. O usuário informa e-mail e senha.
3. O sistema valida as credenciais.
4. O sistema identifica se o usuário é **Aluno** ou **Administrador**.
5. O sistema redireciona o usuário para a interface correspondente.

---

## Fluxos alternativos

### FA1 – Credenciais incorretas

1. No passo 3, o sistema identifica que as credenciais são inválidas.
2. O sistema exibe mensagem de erro.
3. O usuário pode tentar novamente.

### FA2 – Recuperar senha

1. No passo 1, o usuário clica em **“Esqueci minha senha”**.
2. O sistema solicita o e-mail cadastrado.
3. O sistema envia e-mail com instruções de redefinição.

### FA3 – Bloqueio por tentativas excessivas

1. Após múltiplas tentativas inválidas, o sistema bloqueia a conta temporariamente.
2. O usuário deve desbloquear via e-mail ou aguardar o período de liberação.
