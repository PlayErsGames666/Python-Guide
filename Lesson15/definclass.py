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

    def get_data(self): # Метод вывода информации
        print("Dog name: ", self.name, ",", "Age: ", self.age, ",", "Sex: ", self.sex, ",", "Happy: ", self.isHappy, ",", "Colour: ", self.colour)

dog1 = Dog()
dog1.set_data("Dusya", 3, "Male", True, "Grey-Black") # Устанавливаем значения для первой собаки

dog2 = Dog()
dog2.set_data("Jora", 1, "Male", True, "Drak-Blue") # Устанавливаем значения для второй собаки

dog1.get_data() # Вызвает метод print для вывода информации более красиво
dog2.get_data() # Вызвает метод print для вывода информации более красиво
