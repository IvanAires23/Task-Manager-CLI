from db import create_tables
from tasks import add_task

create_tables()

add_task(
    title="Estudar Python",
    description="Terminar projeto do gerenciador de tarefas",
    due_date="2025-06-10",
    priority="alta",
    tags="estudo,programação"
)
