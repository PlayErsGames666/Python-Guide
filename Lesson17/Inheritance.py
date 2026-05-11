# Inheritance то-есть наследование, В прошлом уроке использовали для class Dog
class Building: # Создаём класс Building
    year = None # Задаём параметры год и город
    city = None

    def __init__(self, year, city): # Создаём конструктор который будет запускать данные
        self.year = year
        self.city = city

    def get_info(self): # Создаём метод для вывода данных
        print("Year: ", self.year, ", City: ", self.city)

class School(Building): # Создаём унаслдованный класс School
    pass

school = School(2020, "Tashkent") # Вписываем данные
school.get_info() # Выводим данные
house = Building(2010, "Tokyo")
shop = Building(2026, "Samara")