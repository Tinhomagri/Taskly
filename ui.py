import tkinter as tk
from tkinter import messagebox
from database import add_task, 
import matplotlib.pyplot as plt

def add_task_ui():
    def save_task():
        name = entry_name.get()
        description = entry_description.get("1.0", tk.END)
        due_date = entry_due_date.get()
        priority = combo_priority.get()

        if not name or not due_date or not priority:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")
            return
        
        add_task(name, description, due_date, priority)
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
        window.destroy()

    window = tk.Toplevel()
    window.title("Adicionar Tarefa")
    
    tk.Label(window, text="Nome da Tarefa:").grid(row=0, column=0)
    entry_name = tk.Entry(window)
    entry_name.grid(row=0, column=1)

    tk.Label(window, text="Descrição:").grid(row=1, column=0)
    entry_description = tk.Text(window, height=5, width=30)
    entry_description.grid(row=1, column=1)

    tk.Label(window, text="Data Limite (YYYY-MM-DD):").grid(row=2, column=0)
    entry_due_date = tk.Entry(window)
    entry_due_date.grid(row=2, column=1)

    tk.Label(window, text="Prioridade:").grid(row=3, column=0)
    combo_priority = tk.StringVar(value="Média")
    tk.OptionMenu(window, combo_priority, "Alta", "Média", "Baixa").grid(row=3, column=1)

    tk.Button(window, text="Salvar", command=save_task).grid(row=4, column=1)


def show_dashboard():
    tasks = {'Pendente': 10, 'Concluído': 5, 'Em Andamento': 3}

    labels = tasks.keys()
    sizes = tasks.values()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Resumo de Tarefas")
    plt.show()
