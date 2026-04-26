# try: # открываем обработчик исключений
#     file = open("test.txt", 'r') # задаём параметры открытия, r это чтение
#     file.read() # читаем
# except FileNotFoundError: # так как этого файла нет в папке, он не может его найти
#     print("Файл не найден")
# finally:
    # file.close() # Он не видит переменную file потому что она видно только в блоках try and except

try:
    with open("test.txt", "r", encoding='utf-8') as file: # with as как открывает, так и закрывает файл
        # Даже если вызывается ошибка то файл закрывается
        print(file.read()) # выводит информацию из файла в терминал
except FileNotFoundError: # если файл не будет найден то сработает то что ниже
    print("Файл не найден")