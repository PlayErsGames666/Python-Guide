# if 5 == 5:
#     print("yes")
#     print("!!!")

# user_data = int(input("Input value: "))
#
# isHappy = False
#
# if isHappy and user_data == 6 or user_data == 15:
#     print("User is Happy")
# elif user_data == 5:
#     print("Number is 5")
# elif user_data == 7:
#     print("Number is 7")
# else:
#     print("User is not Happy")

# if user_data != 5:
#     print("Entered")
#     if user_data > 6:
#         print("Number is bigger than 6")

data = input()

number = 5 if data == "Five" else 0

if data == "Five":
    number = 5
else:
    number = 0

print(number)