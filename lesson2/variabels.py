number = 5 #integer int
digit = 4.52343125251 #float
word = 'Result:' #string str
boolean = True #bool
str_num = '5' #string


print(number + int(str_num))

print(word + str(digit))

print(number + float(digit))

print(word, digit + boolean)

print(word + str(boolean))

print(word + str(number + int(str_num)))

del number

number = 5

print("Result", number)