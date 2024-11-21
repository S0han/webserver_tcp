#client file

import socket

#connect the client to the host and port of the server
HOST = '127.0.0.1'
PORT = 8080

#create the client socket that will send data to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall(b"TheKaneologist says Hi!")
data = client_socket.recv(1024)

print(f"Server response received: {data}")

#close connection
client_socket.close()