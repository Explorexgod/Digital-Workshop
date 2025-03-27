import matplotlib.pyplot as plt
import numpy as np

class Derivative:
    def __init__(self):
        self.h = 1e-5  # Малое приращение для численного вычисления производной

    def __get__(self, instance, owner):
        self.instance = instance  # Сохраняем экземпляр ExponentialFunction
        return self  # Возвращаем себя, чтобы можно было вызвать как функцию

    def __call__(self, x):
        """Численно вычисляет производную функции в точке x."""
        f = self.instance  # Получаем доступ к экземпляру ExponentialFunction
        return (f(x + self.h) - f(x - self.h)) / (2 * self.h)

class ExponentialFunction:
    def __init__(self, a):
        self.a = a  # Коэффициент перед экспонентой
        self.derivative = Derivative()  # Создаем экземпляр дескриптора Derivative

    def __call__(self, x):
        """Возвращает значение функции f(x) = a * e^x."""
        return self.a * np.exp(x)

    def plot(self, x_range=(-2, 2)):
        """Строит графики функции f(x) и ее производной f'(x) в заданном диапазоне."""
        x = np.linspace(x_range[0], x_range[1], 400)  # Создаем массив x-значений
        y = self(x)  # Вычисляем значения функции
        y_prime = self.derivative(x)  # Вычисляем значения производной

        plt.figure(figsize=(8, 6))  # Создаем новую фигуру
        plt.plot(x, y, label=f"f(x) = {self.a} * e^x")  # Строим график функции
        plt.plot(x, y_prime, label="f'(x) (производная)")  # Строим график производной

        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("График функции и ее производной")
        plt.legend()  # Отображаем легенду
        plt.grid(True)  # Включаем сетку
        plt.show()  # Отображаем график

# Пример использования
exp_func = ExponentialFunction(a=2.0)
print(exp_func(0))  # Вывод: 2.0
print(exp_func.derivative(0))  # Вывод: (примерно) 2.0 (производная 2e^x в x=0)

# Построение графиков
exp_func.plot()