data = input("Enter the data: ") # Создаём переменную с доступом к записи через терминал

# file = open("data/text2.txt", "w") # Создаём и открываем файл text2.txt
# file = open("data/text2.txt", "a") # работает с английскими символами
file = open("data/text2.txt", "a", encoding="utf-8")  # С дополнительным атрибутом encoding, проблем с русскими символами не будет
file.write(data + '\n') # Записываем в файл данные которые пользователь введёт

file.close() # Закрываем файл

