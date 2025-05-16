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
