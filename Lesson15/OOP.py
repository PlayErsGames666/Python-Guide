class Dog: # Открываем класс в который будем вписывать переменные с параметрами
    name = None # Имя
    age = None # Возраст
    sex = None # Пол
    isHappy = None # Счастлив ли
    colour = None # Цвет

dog1 = Dog() # Даёи запрос в класс Dog(), чтобы задать параметры для dog1
dog1.name = "Dusya"
dog1.age = 3
dog1.isHappy = True
dog1.sex = "Male"
dog1.colour = "Grey-Black"

dog2 = Dog() # Так же для dog2
dog2.name = "Keka"
dog2.age = 1
dog2.isHappy = True
dog2.colour = "Black"
dog2.sex = "Male"

print(dog1.name, dog1.age, dog1.isHappy, dog1.colour) # Выводим имя, возраст, счастлив ли и цвет для dog1
print(dog2.name, dog2.age, dog2.isHappy, dog2.colour) # Выводим имя, возраст, счастлив ли и цвет для dog2