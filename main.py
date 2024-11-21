#server file

import socket

HOST = '127.0.0.1'
PORT = 80

#create the socket --> bind to localhost --> listen on port 80
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

while True:
    (client_socket, address) = server_socket.accept()
    print(f"This is the address: {address}")
    while True:
        #the 1024 is the amount of bytes that will be read AT MOST
        #will block if no data recieved
        data = client_socket.recv(1024)
        if not data: 
            break
        client_socket.sendall(data)
        print(f"Currently recieving data: {data}")

#close connection
server_socket.close()