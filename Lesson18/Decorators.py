import webbrowser # Импортируем встроенный модуль для использования url

def validator(func): # Создаём дикоратор(чаще всего в нём в писывают func)
    def wrapper(url): # Создаём wrapper, обёртку с параметром url
        if "." in url: # Проверка на то, есть ли точка в URL
            func(url) # Если да, то откроет url
        else:
            print("Invalid URL") # Если нет, то выведет это
    return wrapper # необходимо вернуть фунцию wrapper чтобы он работал

@validator # Дикорирум фунцию open_url
def open_url(url): # создаём функцию которую будем использовать как призыв ссылки
    webbrowser.open(url) # от модуля webbrowser открываем url

open_url("https://playersgames666.github.io/Portfolio/") # вписываем нужный url