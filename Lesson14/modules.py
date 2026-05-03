# pypi.org Оффициальный сайт с модулями
# Модули деляться на: Внутренние(которые уже есть в python) и Внешние(на оффициальном сайте, гитхабе или в любом другом месте)

# import time # Импортируем время

# time.sleep(3) # Замараживает программу на определённое количество секунд.
# print("hello") # Только через 3 секунды принтит

# import datetime as d # Импортируем время и дату через as d, тоесть говорить datetime = d
#
# print(d.datetime.now().time()) # Выводит текущее время.
# print(d.datetime.now().date()) # Выводит текущую дату
# print(d.datetime.now().time().minute) # Выводит текущее время в минутых
# print(d.datetime.now().date().month) # Выводит текущую дату в месяцах

# import sys, os, platform
# import random
# import array
#
# # Все модули представлены в интернете
#
# print(sys.path) # Выводит полный путь к текущему проекту
# print(os.name) # Выводит название операционной системы nt(Windows New Technology), posix(MacOS)
# print(platform.system()) # Выводит название платформы системы

from math import sqrt as s # from откуда импортирую и import что импортирую

print(s(100)) # Квадратный корень из 100