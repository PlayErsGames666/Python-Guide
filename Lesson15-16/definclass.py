class Dog: # Открываем класс в который будем вписывать переменные с параметрами
    name = None # Имя
    age = None # Возраст
    sex = None # Пол
    isHappy = None # Счастлив ли
    colour = None # Цвет

    def __init__(self, name = None, age = None, sex = None, isHappy = None, colour = None): # Создаём конструктор __init__
        # self.name = name  # Задаём ему параметры которые есть в class Dog
        # self.age = age
        # self.sex = sex
        # self.isHappy = isHappy
        # self.colour = colour
        self.set_data(name, age, sex, isHappy, colour) # Устанавливает значение, теперь не нужен весь этот верхний код
        self.get_data() # Обращение к методу вывода в терминал

    def set_data(self, name = None, age = None, sex = None, isHappy = None, colour = None): # Создаём метод в class Dog
        # = None теперь базовой значение, если его никто не задаст будет None
        self.name = name # Задаём ему параметры которые есть в class Dog
        self.age = age
        self.sex = sex
        self.isHappy = isHappy
        self.colour = colour
        # self нужен чтобы обращаться к class Dog, без него не будет обршения к наружним переменным

    def get_data(self): # Метод вывода информации
        print("Dog name:", self.name, ",",
              "Age:", self.age, ",",
              "Sex:", self.sex, ",",
              "Happy:", self.isHappy, ",",
              "Colour:", self.colour, ".")

dog1 = Dog("Dusya", 3, "Male", True, "Grey-Black") # Передача данных сразу же в объект
dog1 = Dog() # Теперь и в конструкторе есть =None и не обязательно передавать параметры чтобы код заработал
# dog1.set_data("Dusya", 3, "Male", True, "Grey-Black") # Устанавливаем значения для первой собаки
dog1.set_data("Dusya", 3, "Male", True) # Теперь можно выводить хоть 0  хоть все параметры, проблем не будет

dog2 = Dog("Jora", 1, "Male", True, "Drak-Blue")
# dog2.set_data("Jora", 1, "Male", True, "Drak-Blue") # Устанавливаем значения для второй собаки

# dog1.get_data() # Вызвает метод print для вывода информации более красиво
# dog2.get_data() # Вызвает метод print для вывода информации более красиво
