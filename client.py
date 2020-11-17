import socket
import json

ID = 1
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 53210))

with open('txt', 'r') as file:
    text = ' '.join(file.readlines())

client_sock.sendall(json.dumps({'id': ID, 'text': text}).encode('utf-8'))
response = client_sock.recv(2048)
client_sock.close()

print('Received', json.loads(response)['text'])
