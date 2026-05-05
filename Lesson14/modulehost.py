name = input("Enter name: ") # Ввод имени через теримнал

def hello():
    print("Hello " + name) # Выводим Hello + то что ввели в терминал

def add_three_numbers(a, b, c):
    if a != 0 and b != 0 and c != 0: # Рандомная функция, если а не равен 0, b не равен b тд.
        return a + b + c # Возвращает общую сумму
    else:
        return "some is zero" # Иначе же этот текст