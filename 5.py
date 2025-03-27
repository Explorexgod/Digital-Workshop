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

#2
from fractions import Fraction  # Используем стандартный класс Fraction для удобства


class FractionMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0
        self._validate_matrix()

    def _validate_matrix(self):
        """Проверяет, что матрица прямоугольная и состоит из дробей."""
        if not all(len(row) == self.cols for row in self.matrix):
            raise ValueError("Матрица должна быть прямоугольной.")
        if not all(isinstance(element, Fraction) for row in self.matrix for element in row):
            raise TypeError("Матрица должна содержать только дроби.")

    @classmethod
    def create_zero_matrix(cls, rows, cols):
        """Создает матрицу, заполненную нулями (Fraction(0, 1))."""
        return cls([[Fraction(0, 1) for _ in range(cols)] for _ in range(rows)])

    def __add__(self, other):
        """Сложение матриц."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для сложения.")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return FractionMatrix(result)

    def __sub__(self, other):
        """Вычитание матриц."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для вычитания.")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return FractionMatrix(result)

    def __mul__(self, other):
        """Умножение матриц."""
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.")
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return FractionMatrix(result)

    def transpose(self):
        """Транспонирование матрицы."""
        result = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return FractionMatrix(result)

    # def determinant(self):
    #     """Вычисление определителя (только для квадратных матриц)."""
    #     #TODO: Реализовать вычисление определителя
    #     if self.rows != self.cols:
    #         raise ValueError("Определитель можно вычислить только для квадратных матриц.")
    #     pass  # Реализовать вычисление определителя здесь

    def __str__(self):
        """Красивый вывод матрицы."""
        return '\n'.join([' '.join(str(element) for element in row) for row in self.matrix])

    @staticmethod
    def is_valid_matrix(matrix):
        """Статический метод для проверки валидности матрицы (размеры, тип элементов)."""
        if not isinstance(matrix, list):
            return False
        if not all(isinstance(row, list) for row in matrix):
            return False
        if not all(isinstance(element, Fraction) for row in matrix for element in row):
            return False
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        return all(len(row) == cols for row in matrix)

    def __new__(cls, *args, **kwargs):
        """Пример использования __new__ (можно использовать для логирования создания экземпляров)."""
        instance = super().__new__(cls)
        #print(f"Создается экземпляр {cls.__name__}")
        return instance

    @property
    def shape(self):
        """Свойство, возвращающее размеры матрицы."""
        return (self.rows, self.cols)



# Пример работы:
m1 = FractionMatrix([[Fraction(1, 2), Fraction(1, 3)], [Fraction(2, 5), Fraction(3, 4)]])
m2 = FractionMatrix([[Fraction(1, 3), Fraction(2, 3)], [Fraction(1, 2), Fraction(2, 5)]])

print("Матрица m1:")
print(m1)

print("\nМатрица m2:")
print(m2)

print("\nm1 + m2:")
print(m1 + m2)

print("\nm1 * m2:")
print(m1 * m2)

print("\nТранспонированная m1:")
print(m1.transpose())

print("\nРазмеры m1:")
print(m1.shape)

# print("\nОпределитель m1:")
# print(m1.determinant) #TODO:  Реализовать вычисление определителя
