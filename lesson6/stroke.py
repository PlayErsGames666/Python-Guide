from os.path import split

word = 'lovely,hobby'

print(len(word))

print(word.upper()) # Превращает весь текст в верхний регистр
print(word.isupper()) # Boolean, проверяет весь текст на наличие верхнего регистра True/False

print(word.lower()) # Превращает весь текст в нижний регистр
print(word.islower()) # Boolean, проверяет весь текст на наличие нижнего регистра True/False

print(word.capitalize()) # Делает первую букву в верхнем регистре, а всё остальное в нижнем

print(word.find('b')) # Ищет символы по заданному значению и выводит их индекс

hobby = word.split(',') # Создаёт список из заданных параметров и разделяет их по символу в скобках

# Цикл делающий из обычного два слова через запятую, списком.

for i in range(len(hobby)):
    print(i, hobby[i], hobby)
    hobby[i] = hobby[i].capitalize()

comma = ', '.join(hobby)
print(comma)
print(hobby)