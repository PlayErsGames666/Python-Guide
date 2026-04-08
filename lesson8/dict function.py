country = {'city': 'Moskow', 'district': 'Perovo', 'lang': 'RU', 'population': 1000000}

print(country['city'])
print(country.get('city')) # То же самое только выводит через обычные скобки
# country.clear() # Чистит весь словарь
country.pop('district') # Удаляет только 1 элемент в словаре вместе с его данными
country.popitem() # Удаляет последний элемент в словаре

print(country.keys()) # Полчаем только ключи
print(country.values()) # Получаем только значение

country['city'] = 'NotMoscow' # Изменяем значение ключа city на NotMoscow
print(country.items())

country.update(city='TrueMoscow') # Делает тоже самое, обновляет данные по ключу city на TrueMoscow
print(country.items())