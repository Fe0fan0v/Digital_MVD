from text import Text
import socket
import json

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53210))
serv_sock.listen(10)

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        request = json.loads(client_sock.recv(1024))
        print(request)
        text = Text(request['id'], request['text'])
        if not text:
            # Клиент отключился
            break
        # client_sock.sendall(str.encode(text.performed_text()))

    client_sock.close()
