# Словари или dictionary используется для занесения и сортировки данных по ключам.

country = {'city': 'Tashkent', 'district': 'mirzo-ulugbek', 'lang': 'UZ', 'population': 100000} # Стандратное использование словаря, очень схоже с Redis или JSON
# country = dict(city='Tashkent', district='mirzo-ulugbek', lang='UZ',population=100000) # Используется dict как словарь, минус, из за скобок нельзя использовать кортежи и списки
# print(country['population']) # За раз можно вызвать одно значение
# print(country['city'], country['district']) # Либо же нужно прописывать его снова.

print(country.items()) # создаёт кортедж, тоесть 'ключ', 'значение'

for key, value in country.items():
    print(key, ':', value)

