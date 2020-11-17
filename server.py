from text import Text
import socket
import json
import sqlite3
from datetime import datetime

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53210))
serv_sock.listen(10)


while True:
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        request = json.loads(client_sock.recv(2048))  # получаем запрос
        text_to_work = Text(request['id'], request['text'])  # обрабатываем
        if not text_to_work:  # если нет запроса отключаем
            break
        time = f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'  # собираем и обраб. данные
        date = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'
        text = text_to_work.change_person()

        connection = sqlite3.connect("mvd.sqlite")  # записываем в БД
        cursor = connection.cursor()
        cursor.execute(f"""INSERT INTO documents
                          VALUES (?, ?, ?, ?);""", (int(text_to_work.id), date, time, text))
        connection.commit()
        connection.close()

        client_sock.sendall((json.dumps({'text': text}).encode('utf-8')))  # отправляем ответ клиенту

    client_sock.close()
