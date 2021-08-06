import time
import json
import socket

SERVER = '10.3.168.135'
PORT = 3000
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# read json
# далее данные будут приходить в виде некоторого потока
# BLINK - BLINK
# и сразу будут передаваться, поэтому со стороны клиента будем формировать
# читать и записывать в json лист

with open('data/peers-log.json', 'r', encoding='utf-8') as f:
    mes_full = json.load(f)

# listmes = []
# for mes in mes_full:
#     listmes.append(mes)
# # сохранение листа в json
# with open('data.json','w', encoding='utf-8') as f:
#     json.dump(listmes,f)

server.listen()
print('Waiting')
conn, addr = server.accept()
print('[New Connection]')

while True:
    for mes in mes_full:
        # time.sleep(1)
        data2send = json.dumps(mes).encode()
        conn.sendall(len(data2send).to_bytes(4, "little"))
        conn.sendall(data2send)