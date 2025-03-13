import matplotlib.pyplot as plt
import numpy as np

class Derivative:
    """
    Дескриптор для вычисления производной функции в точке численным методом.
    """
    def __init__(self):
        self.h = 1e-5

    def __get__(self, instance, owner):
        """
        Возвращает объект Derivative как функцию, готовую к вызову.
        """
        self.instance = instance  # Сохраняем экземпляр ExponentialFunction
        return self  # Важно вернуть self, чтобы можно было вызвать __call__

    def __call__(self, x):
        """
        Вычисляет производную функции в точке x численным методом центральной разности.
        """
        return (self.instance(x + self.h) - self.instance(x - self.h)) / (2 * self.h)


class ExponentialFunction:
    """
    Класс для представления экспоненциальной функции вида f(x) = a * e^x.
    """
    def __init__(self, a):
        self.a = a
        self.derivative = Derivative()  # Создаем экземпляр дескриптора

    def __call__(self, x):
        """
        Возвращает значение функции f(x) = a * e^x.
        """
        return self.a * np.exp(x)

    def plot(self):
        """
        Строит графики f(x) и f'(x) в одном окне на интервале x ∈ [-2, 2].
        """
        x = np.linspace(-2, 2, 100)
        y = self(x)
        y_derivative = self.derivative(x)

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=f'f(x) = {self.a} * e^x')
        plt.plot(x, y_derivative, label="f'(x)")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Графики f(x) и f'(x)")
        plt.legend()
        plt.grid(True)
        plt.show()


# Пример использования:
exp_func = ExponentialFunction(a=2)
print(exp_func(0))
print(exp_func.derivative(0))

# Построение графиков
exp_func.plot()