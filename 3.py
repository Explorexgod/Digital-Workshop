#1
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if BankAccount.is_positive(amount):
            self.__balance += amount
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if BankAccount.is_positive(amount):
            if self.__balance >= amount:
                self.__balance -= amount
            else:
                print("Недостаточно средств на счете.")
        else:
            print("Сумма снятия должна быть положительной.")

    def get_balance(self):
        return self.__balance

    @staticmethod
    def is_positive(amount):
        return amount > 0

    @classmethod
    def create_empty_account(cls, account_number):
        return cls(account_number)

#2
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_password(self, password):
        if User.is_strong_password(password):
            self.__password = password
            print("Пароль успешно изменён")
        else:
            print("Ошибка: пароль слишком короткий")

    @staticmethod
    def is_strong_password(password):
        return len(password) >= 6

    @classmethod
    def create_default_user(cls, username):
        default_password = "defaultPassword"  # Минимально безопасный пароль
        if User.is_strong_password(default_password): # Проверка пароля
            return cls(username, default_password)
        else:
            raise ValueError("Дефолтный пароль недостаточно сложный!")

#3
import datetime

class Book:
    def __init__(self, title, author, year):
        if Book.is_valid_year(year):
            self.__title = title
            self.__author = author
            self.__year = year
        else:
            raise ValueError("Некорректный год издания.")

    def get_info(self):
        return f"Название: {self.__title}, автор: {self.__author}, год: {self.__year}"

    @staticmethod
    def is_valid_year(year):
        current_year = datetime.datetime.now().year
        return isinstance(year, int) and year <= current_year

    @classmethod
    def create_default_year(cls, title, author):
        current_year = datetime.datetime.now().year
        return cls(title, author, current_year)