# UC26 – Marcar etapa como concluída

**Ator principal:** Aluno  
**Atores secundários:** –  

---

## Descrição

Este caso de uso descreve como o aluno marca uma etapa de uma trilha como concluída.
Ao marcar uma etapa como concluída, o sistema atualiza o progresso e, se todas as
etapas da trilha estiverem concluídas, marca a trilha como finalizada.

---

## Pré-condições

- O aluno está autenticado no sistema.
- Existe uma trilha de estudos cadastrada com suas etapas (`trails` e `trail_steps`).
- O aluno está vinculado à trilha por meio de um registro em `user_trails`.

---

## Pós-condições

- Existe um registro na tabela `progress` associado ao par (`user_trail_id`, `step_id`)
  com `state = 'done'`.
- O campo `updated_at` da tabela `progress` é atualizado.
- Se todas as etapas da trilha estiverem concluídas, o campo `completed_at` do
  registro correspondente em `user_trails` é preenchido com a data/hora atual.

---

## Fluxo principal

1. O aluno acessa a tela de uma trilha em andamento.
2. O sistema exibe a lista de etapas da trilha e o estado atual de cada uma.
3. O aluno seleciona uma etapa e clica em **“Marcar como concluída”**.
4. O sistema verifica se a etapa pertence à trilha à qual o aluno está vinculado.
5. O sistema verifica se já existe um registro na tabela `progress` para o par
   (`user_trail_id`, `step_id`):
   - Se **não existir**, cria um novo registro com:
     - `state = 'done'`;
     - `score = NULL` (ou o valor informado, se houver avaliação associada).
   - Se **já existir**, atualiza o campo `state` para `done`.
6. O sistema verifica se todas as etapas da trilha associadas àquele `user_trail`
   estão com `state = 'done'`.
7. Se todas as etapas estiverem concluídas, o sistema atualiza o campo
   `completed_at` em `user_trails` com a data/hora atual.
8. O sistema atualiza a interface exibindo a etapa como concluída para o aluno.

---

## Fluxos alternativos

### FA1 – Etapa não pertence à trilha do aluno

1. No passo 4 do fluxo principal, o sistema identifica que a etapa selecionada
   não pertence à trilha associada ao `user_trail` do aluno.
2. O sistema cancela a operação e exibe uma mensagem de erro:
   **“Esta etapa não pertence à trilha selecionada.”**
3. Nenhuma alteração é feita nas tabelas `progress` e `user_trails`.

### FA2 – Aluno não vinculado à trilha

1. No passo 1 do fluxo principal, o sistema não encontra um registro em `user_trails`
   para o par (aluno, trilha).
2. O sistema exibe uma mensagem informando:
   **“Você precisa iniciar esta trilha antes de marcar etapas como concluídas.”**
3. Nenhuma alteração é feita nas tabelas `progress` e `user_trails`.
