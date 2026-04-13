def test_func():
    pass # pass это означает ничего, при включении pass ничего не произойдёт

test_func() # Вызывает саму функцию

def hello():
    print("Hello", end="")
    print("!")

hello()

def hi(word): # Задаётся с параметром word, которое используется только в этой функции
    print(word, end="")
    print("!")

hi("Hi")
hi(5)
hi(True)
hi(0.5)