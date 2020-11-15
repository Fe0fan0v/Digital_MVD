import socket
import json

ID = 1
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 53210))
client_sock.sendall(json.dumps({'id': ID, 'text': 'Hello, world'}).encode('utf-8'))
response = client_sock.recv(1024)
client_sock.close()
print('Received', repr(response))
