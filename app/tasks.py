from db import connect
from tabulate import tabulate


def add_task(title, description, due_date, priority, tags):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, description, due_date, priority, tags)
        VALUES (?, ?, ?, ?, ?)
    """, (title, description, due_date, priority, tags))

    conn.commit()
    conn.close()
    print("Tarefa adicionada com sucesso.")


def list_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, due_date, priority, tags, status FROM tasks"
        )
    tasks = cursor.fetchall()

    conn.close()

    if tasks:
        headers = [
            "ID", "Título", "Vencimento", "Prioridade", "Etiquetas", "Status"
            ]
        print(tabulate(tasks, headers=headers, tablefmt="fancy_grid"))
    else:
        print("Nenhuma tarefa encontrada.")
