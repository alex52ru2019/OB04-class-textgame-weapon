from abc import ABC, abstractmethod
import random

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC): # абстрактный класс оружие
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon): # оружие меч
    weapon_name = "меч"
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon): # оружие лук
    weapon_name = "лук"
    def attack(self):
        return "наносит удар из лука"

class Axe(Weapon): # оружие топор
    weapon_name = "топор"
    def attack(self):
        return "наносит удар топором"

class Spear(Weapon): # оружие копье
    weapon_name = "копье"
    def attack(self):
        return "наносит удар копьем"

# Шаг 3: Модифицируйте класс Fighter
class Fighter: # класс боец
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.weapons = [Sword(), Bow(), Axe(), Spear()]  # Список доступного оружия

    def changeWeapon(self):
        self.weapon = random.choice(self.weapons)
        #print(f"{self.name} выбирает {self.weapon.__class__.__name__.lower()}")
        print(f"{self.name} выбирает {self.weapon.weapon_name}")
    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}")
        else:
            print(f"{self.name} не имеет оружия!")

# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name

# Шаг 4: Реализация боя
def fight(fighter, monster): # можно добавить счетчик здоровья
    if fighter.weapon:
        fighter.attack()
        print(f"{monster.name} побежден!")
    else:
        print(f"{fighter.name} не может атаковать без оружия!")

# Пример использования
fighter = Fighter("Боец Василий")
monster = Monster("Монстр Гоша")

# Боец выбирает случайное оружие и атакует
fighter.changeWeapon()
fight(fighter, monster)

# Боец снова выбирает случайное оружие и атакует
fighter.changeWeapon()
fight(fighter, monster)