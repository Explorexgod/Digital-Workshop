#1
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть нулем.")

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
         return f"Fraction({self.numerator}, {self.denominator})"

    @property
    def value(self):
        return round(self.numerator / self.denominator, 3)

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Нельзя делить на дробь с нулевым числителем.")

        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)


# Пример использования
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(f1.value)