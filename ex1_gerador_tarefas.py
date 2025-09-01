"""

Exercício 1: Gerenciador de tarefas
Crie um programa que funcione como um gerenciador de tarefas simples.
Use um dicionário para armazenar as tarefas. A chave do dicionário
será o nome da tarefa (uma string) e o valor será o status (por exemplo,
"pendente" ou "concluída").

O programa deve ter um menu de opções:
1. Adicionar uma nova tarefa.
2. Marcar uma tarefa como concluída.
3. Ver todas as tarefas.
4. Sair.

"""

tasks: dict[str, str] = dict()


def name_of_task() -> str:
    
    task_name = str(input('Task name: '))
    return task_name

        
def add_new_task(task_name: str) -> None:
    tasks[task_name] = 'Pending'
    print()


def completed_task(task_name: str) -> str:

    if tasks.get(task_name,):
        tasks[task_name] = 'Completed'
        return f'The task "{task_name}" was completed.\n'
    
    return tasks.get(task_name, f'The task "{task_name}" was not founded.\n')


def delete_task(task_name: str) -> str:
    if tasks.get(task_name,):
        del tasks[task_name]
        return f'The task "{task_name}" was successfully deleted.'
    
    return f'The task "{task_name}" was not founded.'


def see_all_tasks() -> None:
    for key, value in tasks.items():
        print(f'{key}: {value}')
    print()


def action() -> int:
    while True:
        try:
            react = int(input(
                '[1] -> Add new task\n'\
                '[2] -> Mark a task as completed\n'\
                '[3] -> See all tasks\n'\
                '[4] -> Delete task\n'\
                '[0] -> Logout\n'
            ))
            print()
            return react
        
        except ValueError:
            print('Please, select 1, 2, 3 or 4!\n')


while True:
    option = action()

    if option == 1:
        add_new_task(name_of_task())

    elif option == 2:
        task_to_complete = completed_task(name_of_task())
        print(task_to_complete)

    elif option == 3:
        see_all_tasks()
    
    elif option == 4:
        task_to_delete = delete_task(name_of_task())
        print(task_to_delete, end='\n\n')

    elif option == 0:
        print('You logged out.\n')
        break

    else:
        print('Invalid option! Try again.\n')
