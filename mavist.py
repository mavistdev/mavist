import requests

class Log():
    def __init__(self):
        print('Successful inited. Use commands from documentation')

    def dislog(whurl = None, content = None, debug = False):
        if whurl == None:
            print('Не заполнено поле URL вебхука')

        elif content == None:
            print('Не заполнено сообщение')

        elif whurl != None and content != None:
            try:
                requests.post(whurl, data = {'content':content})
            except requests.exceptions.MissingSchema:
                print('Отсутствует схема "https://"')
            except requests.exceptions.ConnectionError:
                print('Ошибка подключения к вебхуку. Проверьте URL / интернет соединение')
            except Exception as e:
                print(e)

            if debug:
                print('Post send')

        else:
            print('Неопознанная ошибка.')

    def writefile():
        pass

    def tglog():
        pass
