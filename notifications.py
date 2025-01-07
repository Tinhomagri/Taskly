from twilio.rest import Client
import yagmail
import config


tasks = [
    {"name": "Finalizar Relatório", "due_date": "2025-01-10", "status": "a fazer"},
    {"name": "Reunião com a equipe", "due_date": "2025-01-12", "status": "pendente"},
    {"name": "Enviar email para cliente", "due_date": "2025-01-15", "status": "concluída"}
]


def display_tasks():
    print("\nTarefas:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} - Data: {task['due_date']} - Status: {task['status']}")
    print("\nEscolha o número da tarefa para mais detalhes ou 0 para sair.")


def update_task_status(task_index):
    new_status = input("Digite o novo status da tarefa (a fazer, pendente, concluída): ").lower()
    tasks[task_index]['status'] = new_status
    print(f"Tarefa '{tasks[task_index]['name']}' agora está {new_status}.")


def send_whatsapp_notification(task_name, due_date):
    client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"🚨 Lembrete Importante 🚨\n\n"
             f"Você tem uma tarefa pendente: *{task_name}*\n\n"
             f"📅 A data de conclusão é: *{due_date}*\n\n"
             f"Não deixe para última hora! Fique atento e finalize sua tarefa a tempo! ⏰",
        from_='whatsapp:+14155238886', 
        to='whatsapp:SEUNUMEROAQUI'    
    )
    print("Notificação WhatsApp enviada:", message.sid)


def send_email_notification(email, task_name, due_date):
    yag = yagmail.SMTP(user=config.SENDER_EMAIL, password=config.SENDER_PASSWORD)
    subject = "🚨 Lembrete de Tarefa - Não Esqueça!"
    content = f"""
    Olá! 👋

    Este é um lembrete sobre a tarefa pendente: *{task_name}*.

    📅 Data de Conclusão: *{due_date}*

    Detalhes:
    - Tarefa: {task_name}
    - Data limite para conclusão: {due_date}

    Fique atento para não deixar para última hora! Lembre-se de que sua produtividade depende de suas ações diárias. ⚡

    Atenciosamente,
    Sistema de Notificações Taskly.
    """
    yag.send(to=email, subject=subject, contents=content)
    print("E-mail enviado com sucesso!")


def task_manager():
    while True:
        display_tasks()
        task_choice = int(input("Escolha uma tarefa (número) ou 0 para sair: "))
        
        if task_choice == 0:
            break
        elif 1 <= task_choice <= len(tasks):
            task = tasks[task_choice - 1]
            print(f"\nDetalhes da tarefa: {task['name']}")
            print(f"Data de vencimento: {task['due_date']}")
            print(f"Status atual: {task['status']}")
            action = input("Deseja atualizar o status dessa tarefa? (sim/não): ").lower()
            
            if action == 'sim':
                update_task_status(task_choice - 1)
            send_whatsapp_notification(task['name'], task['due_date'])
            send_email_notification(config.SENDER_EMAIL, task['name'], task['due_date'])
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    task_manager()
