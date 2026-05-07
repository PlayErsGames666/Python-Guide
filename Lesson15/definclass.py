class Dog: # Открываем класс в который будем вписывать переменные с параметрами
    name = None # Имя
    age = None # Возраст
    sex = None # Пол
    isHappy = None # Счастлив ли
    colour = None # Цвет

    def set_data(self, name, age, sex, isHappy, colour): # Создаём метод в class Dog
        self.name = name # Задаём ему параметры которые есть в class Dog
        self.age = age
        self.sex = sex
        self.isHappy = isHappy
        self.colour = colour
        # self нужен чтобы обращаться к class Dog, без него не будет обршения к наружним переменным

dog1 = Dog()
dog1.set_data("Dusya", 3, "Male", True, "Grey-Black")

print(dog1.name)