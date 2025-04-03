import math

class Fraction:
    _instances = {}

    def __new__(cls, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен 0.")
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Числитель и знаменатель должны быть целыми числами.")
        gcd = math.gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        key = (numerator, denominator)
        if key not in cls._instances:
            instance = super().__new__(cls)
            instance.numerator = numerator
            instance.denominator = denominator
            cls._instances[key] = instance
        return cls._instances[key]

    def __init__(self, numerator, denominator):
        pass

    def _reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    @property
    def value(self):
        return round(self.numerator / self.denominator, 3)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Можно складывать только с объектом Fraction.")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Можно вычитать только объект Fraction.")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Можно умножать только на объект Fraction.")

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Деление на ноль недопустимо.")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Можно делить только на объект Fraction.")

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (self.numerator, self.denominator) == (other.numerator, other.denominator)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        raise TypeError("Можно сравнивать только с объектом Fraction.")

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        raise TypeError("Можно сравнивать только с объектом Fraction.")

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __hash__(self):
        return hash((self.numerator, self.denominator))

    @staticmethod
    def is_valid_fraction_string(fraction_string):
        try:
            numerator, denominator = map(int, fraction_string.split('/'))
            return denominator != 0
        except (ValueError, ZeroDivisionError):
            return False

    @classmethod
    def from_string(cls, fraction_string):
        if not cls.is_valid_fraction_string(fraction_string):
            raise ValueError("Недопустимая строка для дроби.")
        numerator, denominator = map(int, fraction_string.split('/'))
        return cls(numerator, denominator)

f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
f3 = Fraction(1,2)

print(f1 == f2)
print(f1 != f2)
print(f1 < f2)
print(f1 > f2)
print(f1 <= f2)
print(f1 >= f2)

print(f1 is f3)

f4 = Fraction.from_string("5/10")
f5 = Fraction(1, 2)

print(f4 is f5)

fractions_set = {f1, f2, f4}
print(len(fractions_set))