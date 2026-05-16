import webbrowser # Импортируем встроенный модуль для использования url

def validator(func):
    def wrapper(url):
        print("До запуска")
        func(url)
        print("После запуска")
    return wrapper

@validator
def open_url(url): # создаём функцию которую будем использовать как призыв ссылки
    webbrowser.open(url) # от модуля webbrowser открываем url

open_url("https://playersgames666.github.io/Portfolio/") # вписываем нужный url