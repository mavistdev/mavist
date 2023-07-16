import requests
import json
import time

helptext_log_dislog = ('Функция dislog.\n'
                       'dislog(webhookurl, message, debug)\n'
                       'webhookurl - ссылка вебхука дискорд\n'
                       'message - сообщение, соответсвтенно\n'
                       'debug - True, если нужно сообщение о том, что запрос отправлен. (не обязательный)\n'
                       'Использование - dislog(\'https://discord.com/...\', \'by mav\')')

helptext_log_vklog = ("Функция vklog.\n"
                      "vklog(token, chatid, message, debug)\n"
                      "token - токен группы\n"
                      "chatid - айди чата. ЦИФРЫ БЕЗ КАВЫЧЕК, ТОЛЬКО INT\n"
                      "message - сообщение, соответсвтенно\n"
                      "debug - True, если нужно сообщение о том, что запрос отправлен. (не обязательный)\n"
                      "Использование - vklog('токен', 2, 'by mav')")

helptext_log_getvkchatids = ("Функция getvkchatids.\n"
                      "getvkchatids(token, num)\n"
                      "token - токен группы\n"
                      "num - Количество айди для проверки. от одного до num, не включяя его.\n"
                      "Использование - getvkchatids('токен', 10). Время на каждый ID - 5 секунд")

class Log():
    def dislog(whurl = None, content = None, debug = False):
        if debug:
            print()

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

    def vklog(token = None, chatid = None, message = None, debug = False):
        try:
            chatid = int(chatid)
        except:
            print('chatid должен содержать только цифры')

        if debug:
            print(helptext_log_vklog)

        elif token == None:
            print('Не указан токен')

        elif chatid == None:
            print('Айди чата не указан')

        elif token != None and chatid != None:
            try:
                requests.post(f'https://api.vk.com/method/messages.send?v=5.103&access_token={token}&chat_id={chatid}&message={message}&random_id=0')
            except requests.exceptions.ConnectionError:
                print('Ошибка подключения к вк. Проверьте URL / интернет соединение')
            except Exception as e:
                print(e)

            if debug:
                print('Post send')

        else:
            print('Неопознанная ошибка.')

    def getvkchatids(token = None, num = 10):
        if token == None:
            print('Не указан токен')
        else:
            try:
                for chatid in range(1, num):
                    if chatid == 2:
                        pass
                    else:
                        try:

                            a = requests.get(
                                f'https://api.vk.com/method/messages.send?v=5.103&access_token={token}&chat_id={chatid}&message=это просто проверка&random_id=0')
                            print(f'{chatid} - {a}')
                            time.sleep(5)
                        except Exception as e:
                            print(e)

                    if num == chatid:
                        break
            except requests.exceptions.ConnectionError:
                print('Ошибка подключения к вк. Проверьте URL / интернет соединение')
            except Exception as e:
                print(e)
