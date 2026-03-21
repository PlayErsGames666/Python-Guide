# nums = [5, 7, 10, 12, 1, 3, True, 'Hello', 6.7, [5, 7]]
# # enter = input('enter number: ')
#
# nums[0] = 50
# nums[6] = nums[3]
# nums[7] = nums[4]
#
# print(nums[-1][1])

numbers = [5, 2 ,7]
# numbers[3] = 100
numbers.append(100)
numbers.append(True) # добавляет значение в конец списка
numbers.insert(1, False) # добавляет в назначенный index, значение

b = [4, 5, 6, 7]
numbers.extend(b) # добавляет значение в конец списка
print(numbers)
numbers.reverse() # переварачивает список
print(numbers)
numbers.sort() #сортировка
print(numbers)
numbers.pop() # удаляет последний элемент в списке
print(numbers)
numbers.pop(0) # удаляет элемент по индексу
print(numbers)
numbers.pop(-2) # удаляет элемент по индексу
print(numbers)
numbers.remove(2) #удаляет по определённому значению
print(numbers)

numbers.clear() # удаляет весь список
print(numbers)

print(numbers.count(True)) # .count() считает сколько таких элементов или значений есть в списке
print(len(numbers)) # показывает длинну всего списка