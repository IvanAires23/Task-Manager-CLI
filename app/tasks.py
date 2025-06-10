from db import connect


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
