tasks = dict()

def name_of_task() -> str:
    
    task_name = str(input('Task name: '))
    return task_name

        
def add_new_task(task_name: str) -> None:
    tasks[task_name] = 'Pendente'
    print()


def completed_task(task_name: str) -> None:
    tasks[task_name] = 'Concluída'
    print()


def delete_task(task_name: str) -> None:
    del tasks[task_name]
    return f'The task {task_name} was successfully deleted.'


def see_all_tasks() -> None:
    for key, value in tasks.items():
        print(f'{key}: {value}')
    print()


def action() -> int:
    while True:
        try:
            react = int(input(
                '[1] -> Add new task\n'\
                '[2] -> Set completed\n'\
                '[3] -> See all tasks\n'\
                '[4] -> Delete task\n'\
                '[0] -> Log out\n'
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
        completed_task(name_of_task())

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
