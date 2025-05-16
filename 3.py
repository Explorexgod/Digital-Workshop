#1
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if self._is_positive_amount(amount):
            self.__balance += amount
        else:
            print("Сумма для пополнения должна быть положительной.")

    def withdraw(self, amount):
        if self._is_positive_amount(amount):
            if self.__balance >= amount:
                self.__balance -= amount
            else:
                print("Недостаточно средств на счете.")
        else:
            print("Сумма для снятия должна быть положительной.")

    def get_balance(self):
        return self.__balance

    @staticmethod
    def _is_positive_amount(amount):
        return amount > 0

    @classmethod
    def create_empty_account(cls, account_number):
        return cls(account_number)


# Пример использования
acc = BankAccount.create_empty_account("123456789")
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())  # Вывод: 300

#2
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_password(self, password):
        if self._is_strong_password(password):
            self.__password = password
            print("Пароль успешно изменен")
        else:
            print("Ошибка: пароль слишком короткий")

    @staticmethod
    def _is_strong_password(password):
        return len(password) >= 6

    @classmethod
    def create_default_user(cls, username):
        return cls(username, "default_password")  # Установите здесь более безопасный пароль по умолчанию

# Пример использования
user = User.create_default_user("Alice")
print(user.get_username())  # Вывод: Alice
user.set_password("12345")  # Ошибка: пароль слишком короткий
user.set_password("securePass")  # Пароль успешно изменен

#3
import datetime

class Book:
    def __init__(self, title, author, year):
        if not isinstance(year, int):
            raise TypeError("Год должен быть целым числом.")
        if not self._is_valid_year(year):
            raise ValueError("Некорректный год издания.")
        self.__title = title
        self.__author = author
        self.__year = year

    def get_info(self):
        return f"{self.__title}, автор: {self.__author}, год: {self.__year}"

    @staticmethod
    def _is_valid_year(year):
        current_year = datetime.datetime.now().year
        return isinstance(year, int) and year <= current_year

    @classmethod
    def create_default_year(cls, title, author):
        return cls(title, author, 2024)


# Пример использования
book1 = Book("1984", "George Orwell", 1949)
print(book1.get_info())  # Вывод: 1984, автор: George Orwell, год: 1949

book2 = Book.create_default_year("Brave New World", "Aldous Huxley")
print(book2.get_info())  # Вывод: Brave New World, автор: Aldous Huxley, год: 2024

# Пример с неверным годом
# book3 = Book("Title", "Author", 2025)  # Вызовет ValueError
6
