import tkinter as tk
from ui import add_task_ui, show_dashboard
from database import create_database

create_database()

root = tk.Tk()
root.title("Taskly - Gerenciador de Tarefas")

tk.Button(root, text="Adicionar Tarefa", command=add_task_ui).pack()
tk.Button(root, text="Resumo de Tarefas", command=show_dashboard).pack()

root.mainloop()
