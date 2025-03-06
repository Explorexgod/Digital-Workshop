#3
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __getattr__(self, item):
        return "This attribute is not available"

# Пример использования:
c = Car("Toyota", "Corolla")
print(c.make)  # Toyota
print(c.color)  # This attribute is not available

#4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            raise AttributeError("Local attributes are not allowed")
        super().__setattr__(key, value)

# Пример использования:
r = Rectangle(10, 20)
r.width = 15  # Успешно
r.height = 25  # Успешно

try:
    r.color = 'red'  # AttributeError: Local attributes are not allowed
except AttributeError as e:
    print(e)