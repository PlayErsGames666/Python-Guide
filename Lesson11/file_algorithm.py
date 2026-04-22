data = input("Enter the data: ") # Создаём переменную с доступом к записи через терминал

# file = open("data/text2.txt", "w") # Создаём и открываем файл text2.txt
file = open("data/text2.txt", "a") # работает с английскими символами

file.write(data + '\n') # Записываем в файл данные которые пользователь введёт

file.close() # Закрываем файл

