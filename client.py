#client file

import socket

HOST = '127.0.0.1'
PORT = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall(b"TheKaneologist says Hi")
data = client_socket(1024)

print(f"Server response received: {data}")