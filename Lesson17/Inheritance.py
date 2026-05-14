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
    pupils = None # Создаём пременную с базовым параметром

    def __init__(self, pupils, year, city): # Вызываем метод конструктор, со всписанными данными из родительского класса Building
        super(School, self).__init__(year, city) # Создаём передачу данных, вызывая супер класс или класс родителя. Используя конструктор из класса родителя передаю данные
        self.pupils = pupils

class House(Building): # Создаём унаслдованный класс House
    pass

class Shop(Building): # Создаём унаслдованный класс Shop
    pass

school = School(100, 2020, "Tashkent") # Вписываем данные
school.get_info() # Выводим данные

house = House(2010, "Tokyo")
house.get_info()

shop = Shop(2026, "Samara")
shop.get_info()