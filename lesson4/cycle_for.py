# for i in range(1, 6, 2):
#     print(i)


# count = 0
# word = "Hello World!"
#
# print(word)
# input = input("Enter a letter: ")
#
# for i in word:
#     if i == input:
#         count += 1
#

# print("Count:", count)

# for i in range(1, 11):
#     if i == 5:
#         break
#
#     if i % 2 == 0:
#         continue
#
#     print(i)

a = input("Type letter: ")
found = False
word = "skill"

# Цикл проверяющий по буквам

for i in word: # word в цикле становиться i
    if i == a: # если i равна a
        found = True  # переменная found будет true
        break # остановка

print(found)