#1
import json

class UserProfile:
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests
    
    def to_dict(self):
        """Преобразует объект UserProfile в словарь"""
        return {
            'name': self.name,
            'age': self.age,
            'interests': self.interests
        }
    
    @classmethod
    def from_dict(cls, data):
        """Создает объект UserProfile из словаря"""
        return cls(data['name'], data['age'], data['interests'])

def save_profile(user, filename):
    """Сохраняет профиль пользователя в файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(user.to_dict(), f, ensure_ascii=False, indent=4)
    except (IOError, OSError) as e:
        print(f"Ошибка при сохранении файла: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

def load_profile(filename):
    """Загружает профиль пользователя из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Проверяем наличие обязательных полей
        if not all(key in data for key in ['name', 'age', 'interests']):
            raise KeyError("Отсутствуют обязательные поля в данных")
            
        return UserProfile.from_dict(data)
    
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON: файл поврежден или содержит невалидный JSON")
    except KeyError as e:
        print(f"Ошибка в структуре данных: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    return None

# Пример использования
if __name__ == "__main__":
    user = UserProfile("Alice", 25, ["Python", "AI"])
    save_profile(user, "profile.json")
    new_user = load_profile("profile.json")
    
    if new_user:
        print(f"Загружен профиль: {new_user.name}, {new_user.age} лет, интересы: {', '.join(new_user.interests)}")

#2
import pickle
import os

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.completed = False
    
    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.name} (приоритет: {self.priority})"

def save_tasks(tasks, filename="tasks.pickle"):
    with open(filename, "wb") as f:
        pickle.dump(tasks, f)

def load_tasks(filename="tasks.pickle"):
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except EOFError:
        return []

def add_task(tasks):
    name = input("Введите название задачи: ")
    while True:
        try:
            priority = int(input("Введите приоритет (целое число): "))
            break
        except ValueError:
            print("Ошибка: приоритет должен быть целым числом")
    
    tasks.append(Task(name, priority))
    save_tasks(tasks)
    print(f"Задача '{name}' добавлена!")

def delete_task(tasks):
    if not tasks:
        print("Список задач пуст!")
        return
    
    print("Список задач:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    
    while True:
        try:
            choice = int(input("Введите номер задачи для удаления: ")) - 1
            if 0 <= choice < len(tasks):
                removed_task = tasks.pop(choice)
                save_tasks(tasks)
                print(f"Задача '{removed_task.name}' удалена!")
                break
            else:
                print("Некорректный номер задачи")
        except ValueError:
            print("Ошибка: введите число")

def complete_task(tasks):
    if not tasks:
        print("Список задач пуст!")
        return
    
    print("Список задач:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    
    while True:
        try:
            choice = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
            if 0 <= choice < len(tasks):
                tasks[choice].completed = True
                save_tasks(tasks)
                print(f"Задача '{tasks[choice].name}' отмечена как выполненная!")
                break
            else:
                print("Некорректный номер задачи")
        except ValueError:
            print("Ошибка: введите число")

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст!")
        return
    
    print("Текущие задачи:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nМеню:")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Отметить задачу как выполненную")
        print("5. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

#3
import json
from typing import Dict, List, Optional

class UserValidator:
    @staticmethod
    def validate_user(user_data: Dict) -> Optional[Dict]:
        """
        Валидирует данные пользователя.
        Возвращает валидные данные или None, если пользователь невалиден.
        """
        try:
            # Проверка наличия обязательных полей
            if 'email' not in user_data:
                raise ValueError("Отсутствует обязательное поле 'email'")
            
            # Проверка типа id (если поле присутствует)
            if 'id' in user_data and not isinstance(user_data['id'], int):
                raise ValueError("Поле 'id' должно быть целым числом")
            
            # Проверка типа name (если поле присутствует)
            if 'name' in user_data and not isinstance(user_data['name'], str):
                raise ValueError("Поле 'name' должно быть строкой")
            
            # Проверка email
            if not isinstance(user_data['email'], str) or '@' not in user_data['email']:
                raise ValueError("Поле 'email' должно быть строкой и содержать символ '@'")
            
            return user_data
        except ValueError as e:
            print(f"Ошибка валидации пользователя: {e}")
            return None

class UserLoader:
    def __init__(self):
        self.loaded_count = 0
        self.skipped_count = 0
    
    def load_users(self, file_path: str) -> List[Dict]:
        """
        Загружает пользователей из JSON-файла с валидацией.
        Возвращает список валидных пользователей.
        """
        valid_users = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                users_data = json.load(file)
                
                if not isinstance(users_data, list):
                    raise ValueError("Ожидается список пользователей в JSON-файле")
                
                for user_data in users_data:
                    validated_user = UserValidator.validate_user(user_data)
                    if validated_user:
                        valid_users.append(validated_user)
                        self.loaded_count += 1
                    else:
                        self.skipped_count += 1
                        
        except FileNotFoundError:
            print(f"Ошибка: файл {file_path} не найден")
        except json.JSONDecodeError:
            print(f"Ошибка: файл {file_path} содержит некорректный JSON")
        except Exception as e:
            print(f"Неожиданная ошибка при загрузке файла: {e}")
        
        return valid_users

    def get_stats(self) -> Dict[str, int]:
        """Возвращает статистику загрузки"""
        return {
            'loaded': self.loaded_count,
            'skipped': self.skipped_count
        }

# Пример использования
if __name__ == "__main__":
    loader = UserLoader()
    users = loader.load_users("users.json")
    
    print("\nЗагруженные пользователи:")
    for user in users:
        print(user)
    
    stats = loader.get_stats()
    print(f"\nСтатистика: загружено {stats['loaded']}, пропущено {stats['skipped']}")

#4
import pickle
from datetime import datetime
from pathlib import Path

class Note:
    def __init__(self, title: str, text: str):
        self.title = title
        self.text = text
        self.creation_date = datetime.now()
    
    def __str__(self):
        return f"{self.title} ({self.creation_date.strftime('%Y-%m-%d %H:%M')})\n{self.text}"

class NoteManager:
    def __init__(self, file_path: str = "notes.pkl"):
        self.file_path = Path(file_path)
        self.notes = []
        self.load_notes()
    
    def add_note(self, title: str, text: str):
        """Добавление новой заметки"""
        new_note = Note(title, text)
        self.notes.append(new_note)
        self.save_notes()
    
    def delete_note(self, index: int):
        """Удаление заметки по индексу"""
        if 0 <= index < len(self.notes):
            del self.notes[index]
            self.save_notes()
        else:
            print("Ошибка: неверный индекс заметки")
    
    def show_all_notes(self):
        """Отображение всех заметок"""
        if not self.notes:
            print("Нет сохраненных заметок")
            return
        
        for i, note in enumerate(self.notes, 1):
            print(f"{i}. {note}\n")
    
    def save_notes(self):
        """Сохранение заметок в файл"""
        try:
            with open(self.file_path, 'wb') as f:
                pickle.dump(self.notes, f)
        except Exception as e:
            print(f"Ошибка при сохранении заметок: {e}")
    
    def load_notes(self):
        """Загрузка заметок из файла"""
        try:
            if self.file_path.exists():
                with open(self.file_path, 'rb') as f:
                    self.notes = pickle.load(f)
        except Exception as e:
            print(f"Ошибка при загрузке заметок: {e}")
            self.notes = []

# Пример использования
if __name__ == "__main__":
    manager = NoteManager()
    
    while True:
        print("\nМенеджер заметок")
        print("1. Показать все заметки")
        print("2. Добавить заметку")
        print("3. Удалить заметку")
        print("4. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            manager.show_all_notes()
        elif choice == "2":
            title = input("Введите заголовок: ")
            text = input("Введите текст заметки: ")
            manager.add_note(title, text)
            print("Заметка добавлена!")
        elif choice == "3":
            manager.show_all_notes()
            if manager.notes:
                try:
                    index = int(input("Введите номер заметки для удаления: ")) - 1
                    manager.delete_note(index)
                    print("Заметка удалена!")
                except ValueError:
                    print("Ошибка: введите число")
        elif choice == "4":
            break
        else:
            print("Неверный ввод, попробуйте еще раз")