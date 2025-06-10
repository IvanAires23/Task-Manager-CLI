from db import create_tables
from tasks import add_task, list_tasks, complete_task

create_tables()

# Se quiser, comente ou descomente essas linhas para testar:

# Cria uma tarefa
add_task(
    title="Finalizar projeto Python",
    description="Implementar todas as funções",
    due_date="2025-06-15",
    priority="alta",
    tags="projeto,python"
)

print("\n--- Tarefas antes de concluir ---")
list_tasks()

# Marca a tarefa 1 como concluída
complete_task(1)

print("\n--- Tarefas depois de concluir ---")
list_tasks()
