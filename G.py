#1
class Animal:
    def speak(self):
        return "издает звук"

class MixinSwim:
    def swim(self):
        return "плавает"

class MixinFly:
    def fly(self):
        return "летает"

class Duck(Animal, MixinSwim, MixinFly):
    def speak(self):
        return "кря-кря"

class Penguin(Animal, MixinSwim):
    def speak(self):
        return "буль-буль"

# Задание
animals = [Duck(), Penguin()]

for animal in animals:
    print(f"{animal.__class__.__name__}:")
    print(f"  Звук: {animal.speak()}")
    print(f"  Движение в воде: {animal.swim()}")
    if hasattr(animal, 'fly'):
        print(f"  В воздухе: {animal.fly()}")
    print("-" * 20)

#2
class Writer:
    def write(self):
        return "пишет текст."

class Painter:
    def draw(self):
        return "рисует картину."

class CreativePerson(Writer, Painter):
    def write(self):
        return "творчески пишет стихотворение."

    def draw(self):
        return "выразительно рисует пейзаж."

# Задание
creative_people = [Writer(), Painter(), CreativePerson()]

for person in creative_people:
    print(f"{person.__class__.__name__}:")
    if hasattr(person, 'write'):
        print(f"  {person.write()}")
    if hasattr(person, 'draw'):
        print(f"  {person.draw()}")
    print("-" * 20)