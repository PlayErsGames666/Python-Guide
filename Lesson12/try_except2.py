try:
    x = int(input("Введите число: ")) # Создаём переменную с input
    x += 5 # для x + 5
    print(x)
except ValueError:
    print("Введите число или цифру")