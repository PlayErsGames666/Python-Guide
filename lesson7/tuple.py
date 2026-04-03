# data = (2, 7, 4, 10, True, -2, 6.5, 'Hello')
# # data[0] = 5 # Переприсваивать значения картежам нельзя
# print(data[1:5])
#
# print(data.count(2))
# print(len(data))
#
# print(data)

# data = 5, 7, 10, "data", True # считается как кортеж
# data = (5) # если в кортеже используется только одно значение, то он не будет являться кортежем
# data = (5,) # если поставить рядом запятую, то он станет кортежем
# data = 5, # тоже считается как кортеж

data = (2, 7, 4, 10, True, -2, 6.5, 'Hello')

for el in data: # Цикл for будет выводить каждый элемент из списка data через абзац
    print(el)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_data = tuple(nums)
word = tuple('Hello World')
print(word)
print(new_data)