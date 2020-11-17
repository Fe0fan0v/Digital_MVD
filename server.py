from text import Text
import socket
import json

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53210))
serv_sock.listen(10)

while True:
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        request = json.loads(client_sock.recv(2048))
        text_to_work = Text(request['id'], request['text'])
        if not text_to_work:
            break
        client_sock.sendall((json.dumps({'text': text_to_work.change_person()}).encode('utf-8')))

    client_sock.close()
