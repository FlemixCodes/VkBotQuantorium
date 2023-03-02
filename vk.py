"""
Код писал FlemixCodes
Github: github.com/FlemixCodes
Vk: vk.com/dmitrylats
"""
import vk_api
from config import TOKEN
from vk_api.longpoll import VkLongPoll, VkEventType

session = vk_api.VkApi(token=TOKEN) # Авторизация по токену
api = session.get_api() # Работа с методами API
longpoll = VkLongPoll(session) # Поднятие LongPoll

print("Успешный запуск бота")

def main():
    while True:
        try:
            for event in longpoll.listen(): # Слушаем сервер
                if event.type == VkEventType.MESSAGE_NEW: # Пришло событие (новое сообщение)
                    if event.to_me: # Пришло для нас
                        message = event.text.lower() # Достаем текст сообщения из события

                        if message == "привет":
                            api.messages.send(peer_id=event.peer_id, message="Привет!", random_id=0)
                        elif message == "пока":
                            api.messages.send(peer_id=event.peer_id, message="Пока!", random_id=0)
                        else:
                            api.messages.send(peer_id=event.peer_id, message="Я вас не понимаю :(", random_id=0)
        except Exception as e:
            print(f"Longpoll Exception: {e}")

if __name__ == "__main__":
    main()
