#1
class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете")
        self._balance -= amount

    def get_interest_rate(self):
        try:
            return 1000 / self._balance
        except ZeroDivisionError:
            raise ZeroDivisionError("Невозможно вычислить процентную ставку при нулевом балансе")

    def __str__(self):
        return f"Баланс счёта: {self._balance:.2f}"


# Пример использования
if __name__ == "__main__":
    account = BankAccount()
    print(account)  # Баланс счёта: 0.00
    
    account.deposit(1000)
    print(account)  # Баланс счёта: 1000.00
    
    account.withdraw(500)
    print(account)  # Баланс счёта: 500.00
    
    try:
        account.withdraw(600)  # Вызовет ошибку
    except ValueError as e:
        print(e)  # Недостаточно средств на счете
    
    try:
        account.deposit(-100)  # Вызовет ошибку
    except ValueError as e:
        print(e)  # Сумма пополнения должна быть положительной
    
    try:
        print(account.get_interest_rate())  # 2.0
        empty_account = BankAccount()
        empty_account.get_interest_rate()  # Вызовет ошибку
    except ZeroDivisionError as e:
        print(e)  # Невозможно вычислить процентную ставку при нулевом балансе

#2
import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        """Конструктор класса с валидацией типов"""
        if not isinstance(real, (int, float)) or not isinstance(imaginary, (int, float)):
            raise TypeError("Real and imaginary parts must be numbers")
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        """Сложение комплексных чисел"""
        if not isinstance(other, ComplexNumber):
            raise TypeError("Can only add ComplexNumber to ComplexNumber")
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __mul__(self, other):
        """Умножение комплексных чисел"""
        if not isinstance(other, ComplexNumber):
            raise TypeError("Can only multiply ComplexNumber by ComplexNumber")
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imag_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imag_part)
    
    def modulus(self):
        """Вычисление модуля комплексного числа"""
        return math.sqrt(self.real**2 + self.imaginary**2)
    
    def __repr__(self):
        """Строковое представление комплексного числа"""
        return f"{self.real} + {self.imaginary}i"


# Пример использования
if __name__ == "__main__":
    print("Демонстрация работы класса ComplexNumber:")
    print("----------------------------------------")
    
    # Создаем комплексные числа
    num1 = ComplexNumber(3, 4)
    num2 = ComplexNumber(1, -2)
    
    print(f"Число 1: {num1}")
    print(f"Число 2: {num2}")
    print(f"Модуль числа 1: {num1.modulus():.2f}")
    print(f"Модуль числа 2: {num2.modulus():.2f}")
    
    # Операции
    sum_result = num1 + num2
    mul_result = num1 * num2
    
    print("\nРезультаты операций:")
    print(f"Сумма: {sum_result}")
    print(f"Произведение: {mul_result}")

#3
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def get_grade(self):
        """Базовый метод для получения оценки"""
        return self.grade
    
    def __str__(self):
        return f"Студент {self.name}, оценка: {self.get_grade()}"
    
    @staticmethod
    def validate_grade(grade):
        """Проверка корректности оценки"""
        if not isinstance(grade, (int, float)):
            raise ValueError("Оценка должна быть числом")
        if grade < 0 or grade > 100:
            raise ValueError("Оценка должна быть в диапазоне от 0 до 100")


class MathStudent(Student):
    def get_grade(self):
        """Переопределенный метод для математиков"""
        self.validate_grade(self.grade)
        
        # Математики оцениваются строже
        if self.grade >= 90:
            return "A (Отлично)"
        elif self.grade >= 75:
            return "B (Хорошо)"
        elif self.grade >= 60:
            return "C (Удовлетворительно)"
        else:
            return "F (Неудовлетворительно)"


class HistoryStudent(Student):
    def get_grade(self):
        """Переопределенный метод для историков"""
        self.validate_grade(self.grade)
        
        # Историки оцениваются мягче
        if self.grade >= 85:
            return "A (Отлично)"
        elif self.grade >= 70:
            return "B (Хорошо)"
        elif self.grade >= 50:
            return "C (Удовлетворительно)"
        else:
            return "F (Неудовлетворительно)"


# Демонстрация полиморфизма
def print_student_info(student):
    """Функция, демонстрирующая полиморфизм"""
    print(student)


# Пример использования
try:
    math_student = MathStudent("Иван Петров", 88)
    history_student = HistoryStudent("Мария Сидорова", 88)
    
    # Вызов одного и того же метода для разных классов
    print_student_info(math_student)     # Выведет оценку по математике
    print_student_info(history_student)  # Выведет оценку по истории
    
    # Проверка обработки исключений
    invalid_student = MathStudent("Ошибка", 150)  # Вызовет исключение
    
except ValueError as e:
    print(f"Ошибка: {e}")

#4
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  # Используем сеттер при инициализации
    
    @property
    def celsius(self):
        """Геттер для температуры в Цельсиях"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Сеттер для температуры в Цельсиях с проверкой типа"""
        if not isinstance(value, (int, float)):
            raise ValueError("Температура должна быть числом")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Геттер для температуры в Фаренгейтах"""
        return self.celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Сеттер для температуры в Фаренгейтах с проверкой типа"""
        if not isinstance(value, (int, float)):
            raise ValueError("Температура должна быть числом")
        self.celsius = (value - 32) * 5/9
    
    def __str__(self):
        """Возвращает строковое представление температуры в обоих форматах"""
        return f"{self.celsius:.2f}°C ({self.fahrenheit:.2f}°F)"


# Пример использования
if __name__ == "__main__":
    print("1. Создаем температуру 0°C:")
    t1 = Temperature(0)
    print(t1)  # 0.00°C (32.00°F)
    
    print("\n2. Устанавливаем 100°C:")
    t1.celsius = 100
    print(t1)  # 100.00°C (212.00°F)
    
    print("\n3. Устанавливаем 32°F:")
    t2 = Temperature(0)
    t2.fahrenheit = 32
    print(t2)  # 0.00°C (32.00°F)
    
    print("\n4. Пробуем установить нечисловое значение:")
    try:
        t3 = Temperature("hot")
    except ValueError as e:
        print(f"Ошибка: {e}")  # Температура должна быть числом

#5
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой")
        if len(value) == 0:
            raise ValueError("Название не может быть пустым")
        self._name = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом")
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value
    
    def get_discounted_price(self, discount):
        if not isinstance(discount, (int, float)):
            raise TypeError("Скидка должна быть числом")
        if discount < 0:
            raise ValueError("Скидка не может быть отрицательной")
        if discount >= 100:
            raise ValueError("Скидка не может быть 100% или более")
        
        return self.price * (1 - discount / 100)
    
    def __str__(self):
        return f"{self.name} - {self.price} руб."


class Book(Product):
    def __init__(self, name, author, price, pages):
        super().__init__(name, price)
        self.author = author
        self.pages = pages
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("Автор должен быть строкой")
        if len(value) == 0:
            raise ValueError("Автор не может быть пустым")
        self._author = value
    
    @property
    def pages(self):
        return self._pages
    
    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value
    
    def __str__(self):
        return f"Книга: {super().__str__()}, автор: {self.author}, страниц: {self.pages}"


class EBook(Book):
    def __init__(self, name, author, price, pages, file_size, file_format):
        super().__init__(name, author, price, pages)
        self.file_size = file_size
        self.file_format = file_format
    
    @property
    def file_size(self):
        return self._file_size
    
    @file_size.setter
    def file_size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Размер файла должен быть числом")
        if value <= 0:
            raise ValueError("Размер файла должен быть положительным")
        self._file_size = value
    
    @property
    def file_format(self):
        return self._file_format
    
    @file_format.setter
    def file_format(self, value):
        if not isinstance(value, str):
            raise TypeError("Формат файла должен быть строкой")
        if len(value) == 0:
            raise ValueError("Формат файла не может быть пустым")
        self._file_format = value
    
    def __str__(self):
        return f"Электронная книга: {super().__str__()}, размер: {self.file_size} MB, формат: {self.file_format}"


# Демонстрационный блок с try-except-finally
try:
    # Создаем обычную книгу
    book = Book("Война и мир", "Лев Толстой", 1500, 1225)
    print(book)
    
    # Создаем электронную книгу
    ebook = EBook("1984", "Джордж Оруэлл", 899, 328, 5.2, "PDF")
    print(ebook)
    
    # Проверяем скидку
    print(f"Цена со скидкой 20%: {book.get_discounted_price(20)} руб.")
    print(f"Цена со скидкой 50%: {ebook.get_discounted_price(50)} руб.")
    
    # Проверяем обработку ошибок (раскомментируйте для проверки)
    # invalid_book = Book("", "Автор", 100, 100)  # Вызовет ValueError
    # invalid_discount = book.get_discounted_price(-10)  # Вызовет ValueError
    # invalid_discount2 = book.get_discounted_price(110)  # Вызовет ValueError

except TypeError as e:
    print(f"Ошибка типа: {e}")
except ValueError as e:
    print(f"Ошибка значения: {e}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
finally:
    print("Демонстрация завершена")

#6
class Whiteboard:
    def __init__(self):
        self.__messages = []
    
    def add_message(self, msg):
        if not isinstance(msg, str):
            raise TypeError("Сообщение должно быть строкой")
        self.__messages.append(msg)
    
    def __add__(self, other):
        if not isinstance(other, Whiteboard):
            raise TypeError("Можно объединять только с другой доской")
        new_board = Whiteboard()
        new_board.__messages = self.__messages + other.__messages
        return new_board
    
    def __len__(self):
        return len(self.__messages)
    
    def __call__(self):
        for msg in self.__messages:
            print(msg)
    
    @property
    def latest_message(self):
        if not self.__messages:
            return None
        return self.__messages[-1]
    
    @latest_message.setter
    def latest_message(self, value):
        if not isinstance(value, str):
            raise TypeError("Сообщение должно быть строкой")
        if not self.__messages:
            self.__messages.append(value)
        else:
            self.__messages[-1] = value


# Демонстрация работы класса с обработкой исключений
try:
    # Создаем две доски
    board1 = Whiteboard()
    board2 = Whiteboard()
    
    # Добавляем сообщения
    board1.add_message("Первое сообщение")
    board1.add_message("Второе сообщение")
    board2.add_message("Третье сообщение")
    
    # Тестируем магические методы
    print(f"Количество сообщений в board1: {len(board1)}")  # 2
    print(f"Последнее сообщение board1: {board1.latest_message}")  # "Второе сообщение"
    
    # Изменяем последнее сообщение
    board1.latest_message = "Измененное второе сообщение"
    print(f"Измененное последнее сообщение: {board1.latest_message}")
    
    # Объединяем доски
    combined_board = board1 + board2
    print("\nСодержимое объединенной доски:")
    combined_board()  # Выводит все сообщения
    
    # Тестируем обработку ошибок
    print("\nПопытка добавить не строку:")
    board1.add_message(123)  # Вызовет TypeError
    
except TypeError as e:
    print(f"Ошибка: {e}")
finally:
    print("\nДемонстрация завершена (блок finally)")

#7
class Function:
    def __call__(self, x):
        """Вычисляет значение функции в точке x"""
        try:
            if not isinstance(x, (int, float)):
                raise TypeError("x должен быть числом")
            return self._calculate(x)
        except TypeError as e:
            print(f"Ошибка: {e}")
            return None
        finally:
            pass  # Можно добавить код, который выполнится в любом случае

    def _calculate(self, x):
        """Метод для переопределения в дочерних классах"""
        raise NotImplementedError("Метод должен быть переопределен в дочернем классе")

    def __str__(self):
        """Строковое представление функции"""
        return "Базовая функция"

    def __eq__(self, other):
        """Сравнение функций по значению в точке x=1"""
        if not isinstance(other, Function):
            return NotImplemented
        return self(1) == other(1)

    def __lt__(self, other):
        """Сравнение функций по значению в точке x=1"""
        if not isinstance(other, Function):
            return NotImplemented
        return self(1) < other(1)


class LinearFunction(Function):
    def __init__(self, a, b):
        if not all(isinstance(coef, (int, float)) for coef in [a, b]):
            raise TypeError("Коэффициенты должны быть числами")
        self.a = a
        self.b = b

    def _calculate(self, x):
        return self.a * x + self.b

    def __str__(self):
        return f"Линейная функция: {self.a}x + {self.b}"


class QuadraticFunction(Function):
    def __init__(self, a, b, c):
        if not all(isinstance(coef, (int, float)) for coef in [a, b, c]):
            raise TypeError("Коэффициенты должны быть числами")
        self.a = a
        self.b = b
        self.c = c

    def _calculate(self, x):
        return self.a * x**2 + self.b * x + self.c

    def __str__(self):
        return f"Квадратичная функция: {self.a}x² + {self.b}x + {self.c}"


# Примеры использования
if __name__ == "__main__":
    # Создаем функции
    linear = LinearFunction(2, 3)
    quadratic = QuadraticFunction(1, 2, 3)
    
    # Вычисляем значения
    print(f"{linear}(5) = {linear(5)}")  # 2*5 + 3 = 13
    print(f"{quadratic}(2) = {quadratic(2)}")  # 1*4 + 2*2 + 3 = 11
    
    # Проверяем сравнение функций по значению в точке x=1
    print(f"{linear}(1) = {linear(1)}")  # 5
    print(f"{quadratic}(1) = {quadratic(1)}")  # 6
    print(f"linear == quadratic: {linear == quadratic}")  # False
    print(f"linear < quadratic: {linear < quadratic}")  # True
    
    # Проверка обработки ошибок
    print(linear("не число"))  # Выведет сообщение об ошибке

#8
from abc import ABC, abstractmethod

class Customer:
    def __init__(self, name, email):
        self._name = name
        self._email = email
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой")
        self._name = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email должен быть строкой")
        self._email = value
    
    def __str__(self):
        return f"Клиент: {self.name}, Email: {self.email}"

class Order:
    def __init__(self):
        self._items = []
        self._prices = []
    
    def add_item(self, item, price):
        if not isinstance(item, str):
            raise TypeError("Название товара должно быть строкой")
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        
        self._items.append(item)
        self._prices.append(price)
    
    def get_total(self):
        if not self._items:
            raise ValueError("Заказ пуст")
        return sum(self._prices)
    
    def __str__(self):
        items_str = "\n".join(f"{item}: {price} руб." for item, price in zip(self._items, self._prices))
        return f"Заказ:\n{items_str}\nИтого: {self.get_total()} руб."

class LoggedEntity(ABC):
    def __init__(self):
        self._log = []
    
    @property
    def log(self):
        return self._log.copy()
    
    @abstractmethod
    def log_action(self, action):
        pass

class OrderWithLogging(Order, LoggedEntity):
    def __init__(self):
        Order.__init__(self)
        LoggedEntity.__init__(self)
        self.log_action("Создан новый заказ с логированием")
    
    def add_item(self, item, price):
        try:
            super().add_item(item, price)
            self.log_action(f"Добавлен товар: {item} по цене {price} руб.")
        except (TypeError, ValueError) as e:
            self.log_action(f"Ошибка при добавлении товара: {str(e)}")
            raise
    
    def get_total(self):
        try:
            total = super().get_total()
            self.log_action(f"Запрошена сумма заказа: {total} руб.")
            return total
        except ValueError as e:
            self.log_action(f"Ошибка при расчете суммы: {str(e)}")
            raise
    
    def log_action(self, action):
        self._log.append(action)
    
    def __str__(self):
        order_info = Order.__str__(self) if self._items else "Заказ пуст"
        log_info = "\n".join(self.log[-3:]) if self.log else "Логи отсутствуют"
        return f"{order_info}\n\nПоследние действия:\n{log_info}"

# Демонстрационный блок
if __name__ == "__main__":
    try:
        customer = Customer("Иван Иванов", "ivan@example.com")
        print(customer)
        
        order = OrderWithLogging()
        
        order.add_item("Книга", 500)
        order.add_item("Флешка", 800)
        
        print("\nИнформация о заказе:")
        print(order)
        
        print("\nСумма заказа:", order.get_total())
        
        # Проверка ошибок
        # order.add_item(123, 500)  # TypeError
        # order.add_item("Телефон", -100)  # ValueError
        # empty_order = OrderWithLogging()
        # empty_order.get_total()  # ValueError
        
    except Exception as e:
        print(f"\nПроизошла ошибка: {str(e)}")
    finally:
        print("\nПрограмма завершена")
