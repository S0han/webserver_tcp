import socket

HOST = '127.0.0.1'
PORT = 80

#create the socket --> bind to localhost --> listen on port 80
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)