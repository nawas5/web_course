import json
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = '10.3.168.135'
PORT = 3000
ADDR = (SERVER, PORT)

# client.connect(ADDR)

# можно ли через dash чтобы выводились данные в консоль