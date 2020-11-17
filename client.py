import socket
import json

ID = 1
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # соединяем
client_sock.connect(('127.0.0.1', 53210))

with open('txt', 'r') as file:
    text = ' '.join(file.readlines())  # читаем из файла

client_sock.sendall(json.dumps({'id': ID, 'text': text}).encode('utf-8'))  # отправляем на сервер данные
response = client_sock.recv(2048)  # получаем ответ от сервера
client_sock.close()

print('Received', json.loads(response)['text'])
