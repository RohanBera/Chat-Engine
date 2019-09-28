import socket

host = '10.5.1.84'
port = 9000

srv_sock = socket.socket() # creates a socket
srv_sock.bind((host, port))
# while True:
srv_sock.listen()

conn, addr = srv_sock.accept()
print("connection established : "+ str(addr))
while True :
    data = conn.recv(1024).decode()
    print("from client: " +str(data))
    data = input(' => ')
    conn.send(data.encode())

conn.close()

