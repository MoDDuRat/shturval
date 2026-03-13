from task_storage import TaskStorage

def main(storage=None):
    if storage is None:
        storage = TaskStorage()

    while True:
        print("\n-- Менеджер задач ---")
        print("1. Добавить новую задачу")
        print("2. Показать все задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выход")

        choice = input("Выбери действие (1-5): ")

        if choice == '1':
            description = input("Введи описание задачи: ")
            storage.add_task(description)
            print("Задача успешно добавлена.")
            
        elif choice == '2':
            storage.get_all_tasks()
            
        elif choice == '3':
            try:
                task_id = int(input("Введи ID задачи для завершения: "))
                storage.complete_task(task_id)
                print("Задача отмечена как выполненная.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")
                
        elif choice == '4':
            try:
                task_id = int(input("Введи ID задачи для удаления: "))
                storage.remove_task(task_id)
                print("Задача удалена.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")
                
        elif choice == '5':
            print("Выход...")
            break
            
        else:
            print("Неверный ввод, попробуй снова.")

if __name__ == "__main__":
    main()

    # Колесниченко лучший <3
