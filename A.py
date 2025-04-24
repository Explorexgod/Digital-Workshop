#1
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    __slots__ = ('x', 'y', '_z')  # Ограничиваем атрибуты

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        raise AttributeError("Координата z неизменяема")

# Тестовый сценарий (для проверки работы):
pt3 = Point3D(10, 20, 30)

print(f"x = {pt3.x}, y = {pt3.y}, z = {pt3.z}")

try:
    pt3.z = 40
except AttributeError as e:
    print(f"Ошибка при попытке изменить z: {e}")

try:
    pt3.extra = 100
except AttributeError as e:
    print(f"Ошибка при попытке добавить новый атрибут: {e}")

try:
    print(pt3.__dict__)
except AttributeError as e:
    print(f"Ошибка при обращении к __dict__: {e}")

#2
import timeit
import sys

class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx):
        self.x += dx

class SlotPoint:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx):
        self.x += dx

def benchmark(num_instances, num_iterations):
    # Создание экземпляров
    normal_points = [NormalPoint(i, i) for i in range(num_instances)]
    slot_points = [SlotPoint(i, i) for i in range(num_instances)]

    # Замер времени для NormalPoint
    normal_time = timeit.timeit(lambda: [p.move(1) for p in normal_points], number=num_iterations)

    # Замер времени для SlotPoint
    slot_time = timeit.timeit(lambda: [p.move(1) for p in slot_points], number=num_iterations)

    return normal_time, slot_time, normal_points[0], slot_points[0]

if __name__ == "__main__":
    num_instances = 1000
    num_iterations = 100

    normal_time, slot_time, normal_point_instance, slot_point_instance = benchmark(num_instances, num_iterations)

    print(f"Время для NormalPoint: {normal_time:.4f} сек")
    print(f"Время для SlotPoint: {slot_time:.4f} сек")

    # Сравнение размеров в памяти
    normal_size = sys.getsizeof(normal_point_instance)
    slot_size = sys.getsizeof(slot_point_instance)

    print(f"Размер в памяти NormalPoint: {normal_size} байт")
    print(f"Размер в памяти SlotPoint: {slot_size} байт")

    # Дополнительная проверка на невозможность добавления новых атрибутов в SlotPoint
    try:
        slot_point_instance.extra = 10  # Попытка добавить новый атрибут
    except AttributeError as e:
        print(f"Поймано исключение: {e}")
    else:
        print("Ошибка: удалось добавить новый атрибут в SlotPoint!")

#3
class Student:
    __slots__ = ('name', 'age', 'grade')

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def calculate_average_grade(students):
    """Вычисляет среднюю оценку студентов в списке."""
    if not students:
        return 0  # Обработка пустого списка

    total_grade = sum(student.grade for student in students)
    return total_grade / len(students)

# Создание коллекции студентов
students = [
    Student("Alice", 20, 90),
    Student("Bob", 22, 75),
    Student("Charlie", 19, 85),
    Student("David", 21, 95)
]

# Вычисление средней оценки
average_grade = calculate_average_grade(students)

# Вывод результата
print(f"Средняя оценка студентов: {average_grade}")

# Попытка добавить новый атрибут (для демонстрации __slots__)
try:
    students[0].city = "New York"  # Попытка добавить атрибут
except AttributeError as e:
    print(f"Поймано исключение: {e}")

#4
class Product:
    __slots__ = ('name', 'price', 'quantity')

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def find_expensive_products(products, price_threshold):
    """
    Возвращает список названий товаров, цена которых превышает заданный порог.

    Args:
        products (dict): Словарь, где ключи - названия товаров, а значения - объекты Product.
        price_threshold (float): Пороговая цена.

    Returns:
        list: Список названий товаров, цена которых выше пороговой.
    """
    expensive_products = [
        name for name, product in products.items() if product.price > price_threshold
    ]
    return expensive_products

# Создание словаря товаров
products = {
    "Laptop": Product("Laptop", 1200.00, 10),
    "Mouse": Product("Mouse", 25.00, 50),
    "Keyboard": Product("Keyboard", 75.00, 30),
    "Monitor": Product("Monitor", 300.00, 15)
}

# Задаем пороговую цену
price_threshold = 100.00

# Находим товары, цена которых превышает пороговую
expensive_product_names = find_expensive_products(products, price_threshold)

# Выводим результаты
print(f"Товары с ценой выше {price_threshold}: {expensive_product_names}")

# Попытка добавить новый атрибут (для демонстрации __slots__)
try:
    products["Laptop"].category = "Electronics"  # Попытка добавить атрибут
except AttributeError as e:
    print(f"Поймано исключение: {e}")