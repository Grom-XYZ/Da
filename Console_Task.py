import os

def load_tasks(filename="tasks.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]
    
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines([task + "\n" for task in tasks])

def display_tasks(tasks):
    if not tasks:
        print("Пусто")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Введи новую задачу:")
    tasks.append(task)
    print("Задача добовлена!")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Что удалить:"))
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Задача '{removed}' удаленно.")
        else:
            print("Неправильно")
    except ValueError:
        print("Введи число.")

def mark_done(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Введи номер выполненной задачи:")) - 1
        if 0 <= index < len(tasks):
            tasks[index] += "[Выполненно]"
            print(f"Задача 'removed' удаленно.")
        else:
            print("Неправильно")
    except ValueError:
        print("Введи число.")

def clear_tasks():
    confirm = input("Ты точен хочешь очистить список? Ты ведь его больше не увидешь. (да\нет)")
    if confirm.lower() == "да":
        return []
    return None
    
def main():
    tasks = load_tasks()
    while True:
        print("\nМеню")
        print("1. Показать задачи. ")
        print("2. Добавить задачу. ")
        print("3. Удалить задачу. ")
        print("4. Отметить задачу как выполненную. ")
        print("5. Очистить список залач ")
        print("6. Загрузить задачу из файла. ")
        print("7. Выйти. ")
        choise = input("Введи (1-7):")
        if choise == "1":
            display_tasks(tasks)
        elif choise == "2":
            add_task(tasks)
        elif choise == "3":
            remove_task(tasks)
        elif choise == "4":
            mark_done(tasks)
        elif choise == "5":
            new_tasks = clear_tasks()
            if new_tasks is not None:
                tasks = new_tasks
                print("Очищенно.")
        elif choise == "6":
            tasks = load_tasks()
            print("Добавлен.")
        elif choise == "7":
            save_tasks(tasks)
            print(" Сохранение...")
            break
        else:
            print("Неправильно")

if __name__ == "__main__":
    main()