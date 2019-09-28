import socket

host = '10.5.0.230'
port = 5000

srv_sock = socket.socket() # creates a socket
srv_sock.bind(host, port)
srv_sock.listen()


