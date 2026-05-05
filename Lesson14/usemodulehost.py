# import modulehost as mhost # Используем созданный модуль как mhost
#
# print(mhost.name) # выводим mhost и вводим имя
# mhost.hello() # автоматически выводит hello и имя

from modulehost import add_three_numbers as atn # импортируем ту функцию с сложением

print(atn(10, 20, 30)) # задаём параметры для нашей функции