import json
import os
import subprocess

def execute_command(command, arguments):
    if command == "list_files":
        list_files()
    elif command == "create_file":
        create_file(arguments)
    elif command == "delete_file":
        delete_file(arguments)
    elif command == "rename_file":
        rename_file(arguments)
    elif command == "search_files":
        search_files(arguments)
    else:
        print(f"Неизвестная команда: {command}")

def list_files():
    files = os.listdir()
    for file in files:
        print(file)

def create_file(arguments):
    filename = arguments.get("filename")
    if filename:
        with open(filename, 'w') as file:
            print(f"Файл {filename} создан")
    else:
        print("Не указано имя файла для создания.")

def delete_file(arguments):
    filename = arguments.get("filename")
    if filename:
        try:
            os.remove(filename)
            print(f"Файл {filename} удален")
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
    else:
        print("Не указано имя файла для удаления.")

def rename_file(arguments):
    old_name = arguments.get("old_name")
    new_name = arguments.get("new_name")
    if old_name and new_name:
        try:
            os.rename(old_name, new_name)
            print(f"Файл {old_name} переименован в {new_name}")
        except FileNotFoundError:
            print(f"Файл {old_name} не найден")
    else:
        print("Не указаны имена файлов для переименования.")

def search_files(arguments):
    search_type = arguments.get("type")
    if search_type == "mask":
        mask = arguments.get("mask")
        if mask:
            subprocess.run(["find", "-name", f"*{mask}*"])
        else:
            print("Не указана маска для поиска.")
    elif search_type == "extension":
        extension = arguments.get("extension")
        if extension:
            subprocess.run(["find", "-name", f"*.{extension}"])
        else:
            print("Не указано расширение для поиска.")
    elif search_type == "date":
        date = arguments.get("date")
        if date:
            try:
                subprocess.run(["find", "-type", "f", "-newermt", date])
            except ValueError:
                print("Неверный формат даты.")
        else:
            print("Не указана дата для поиска.")
    elif search_type == "size":
        size = arguments.get("size")
        if size:
            subprocess.run(["find", "-type", "f", "-size", f"+{size}c"])
        else:
            print("Не указан размер для поиска.")
    else:
        print("Неизвестный тип поиска.")

def main():
    json_file = input("Введите путь к JSON файлу: ")
    try:
        with open(json_file, 'r') as file:
            commands = json.load(file)
            for command, arguments in commands.items():
                print(f"Выполнение команды: {command}")
                execute_command(command, arguments)
    except FileNotFoundError:
        print("Указанный JSON файл не найден.")

if __name__ == "__main__":
    main()
