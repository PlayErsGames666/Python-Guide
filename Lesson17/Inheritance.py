# Inheritance то-есть наследование, В прошлом уроке использовали для class Dog
class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self, year, city):
        print("Year: ", self.year, "City: ", self.city)


