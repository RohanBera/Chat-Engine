import socket
from multiprocess import Process
from platform import python_version
from os import system

def server_start(port):
    vers='python'+python_version().split('.')[0]
    system(vers + ' -m http.server ' + port)

host = '10.5.1.84'
port = 9000
Max_Connections = 5

try :
    srv_sock = socket.socket() # creates a socket
    print("Socket is created.!")
except Exception as e :
    print("Error while creating a socket: ", e)

par_process = Proces(target = server_start(port))
par_process.start()
par_process.join()
    
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

