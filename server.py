import socket

host = '10.5.1.84'
port = 9000
Max_Connections = 5

try :
    srv_sock = socket.socket() # creates a socket
    print("Socket is created.!")
except Exception as e :
    print("Error while creating a socket: ", e)
   
try :
    srv_sock.bind((host, port))
    print("Socket is bound to Host IP: ", host, " and Port: ", port)
except Exception as e :
    print("Error while binding the socket: ", e)
# while True:
srv_sock.listen(Max_connections)

conn, addr = srv_sock.accept()
print("connection established : "+ str(addr))
while True :
    data = conn.recv(1024).decode()
    print("from client: " +str(data))
    data = input(' => ')
    conn.send(data.encode())

conn.close()

