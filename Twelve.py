import os
import subprocess

def display_menu():
    print("\nВыберите действие:")
    print("1. Просмотр содержимого текущей директории")
    print("2. Создание файла")
    print("3. Удаление файла")
    print("4. Переименование файла")
    print("5. Поиск файлов")
    print("6. Выход")

def list_files():
    files = os.listdir()
    for file in files:
        print(file)

def create_file():
    filename = input("Введите имя файла для создания: ")
    with open(filename, 'w') as file:
        print(f"Файл {filename} создан")

def delete_file():
    filename = input("Введите имя файла для удаления: ")
    try:
        os.remove(filename)
        print(f"Файл {filename} удален")
    except FileNotFoundError:
        print(f"Файл {filename} не найден")

def rename_file():
    old_name = input("Введите текущее имя файла: ")
    new_name = input("Введите новое имя файла: ")
    try:
        os.rename(old_name, new_name)
        print(f"Файл {old_name} переименован в {new_name}")
    except FileNotFoundError:
        print(f"Файл {old_name} не найден")

def search_files():
    print("Выберите параметр поиска:")
    print("1. По маске")
    print("2. По расширению")
    print("3. По дате")
    print("4. По размеру")
    choice = input("Ваш выбор: ")

    if choice == "1":
        mask = input("Введите маску для поиска: ")
        subprocess.run(["find", "-name", f"*{mask}*"])
    elif choice == "2":
        extension = input("Введите расширение для поиска: ")
        subprocess.run(["find", "-name", f"*.{extension}"])
    # Добавьте обработку других параметров поиска (дата, размер) по аналогии

def main():
    while True:
        display_menu()
        choice = input("Ваш выбор: ")
        if choice == "1":
            list_files()
        elif choice == "2":
            create_file()
        elif choice == "3":
            delete_file()
        elif choice == "4":
            rename_file()
        elif choice == "5":
            search_files()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
