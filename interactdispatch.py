import subprocess
import psutil

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, command):
        self.tasks.append({"name": name, "command": command, "process": None})

    def list_tasks(self):
        print("Список задач:")
        for idx, task in enumerate(self.tasks, start=1):
            if task["process"] is not None and task["process"].is_running():
                print(f"{idx}. {task['name']} (запущена)")
            else:
                print(f"{idx}. {task['name']} (остановлена)")

    def start_task(self, task_idx):
        task = self.tasks[task_idx - 1]
        if task["process"] is None or not task["process"].is_running():
            task["process"] = subprocess.Popen(task["command"], shell=True)
            print(f"Задача '{task['name']}' запущена.")
        else:
            print(f"Задача '{task['name']}' уже запущена.")

    def stop_task(self, task_idx):
        task = self.tasks[task_idx - 1]
        if task["process"] is not None and task["process"].is_running():
            task["process"].terminate()
            task["process"] = None
            print(f"Задача '{task['name']}' остановлена.")
        else:
            print(f"Задача '{task['name']}' уже остановлена или не была запущена.")

def main():
    task_manager = TaskManager()

    # Добавление задач
    task_manager.add_task("Программа 1", "python program1.py")
    task_manager.add_task("Программа 2", "python program2.py")
    task_manager.add_task("Программа 3", "python program3.py")

    while True:
        print("\nВыберите действие:")
        print("1. Список задач")
        print("2. Запуск задачи")
        print("3. Остановка задачи")
        print("4. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            task_manager.list_tasks()
        elif choice == "2":
            task_manager.list_tasks()
            task_idx = int(input("Введите номер задачи для запуска: "))
            if 1 <= task_idx <= len(task_manager.tasks):
                task_manager.start_task(task_idx)
            else:
                print("Неверный номер задачи.")
        elif choice == "3":
            task_manager.list_tasks()
            task_idx = int(input("Введите номер задачи для остановки: "))
            if 1 <= task_idx <= len(task_manager.tasks):
                task_manager.stop_task(task_idx)
            else:
                print("Неверный номер задачи.")
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
