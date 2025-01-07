import sqlite3

def create_database():
    conn = sqlite3.connect('taskly.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            due_date DATE NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_task(name, description, due_date, priority, status="Pendente"):
    conn = sqlite3.connect('taskly.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (name, description, due_date, priority, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, description, due_date, priority, status))
    conn.commit()
    conn.close()
