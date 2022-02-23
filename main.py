import os
import db
import requests
import time
import wikipedia
import subprocess
from function import *


def take_input():
	while True:
		inp = subprocess.getoutput("termux-speech-to-text")
		time.sleep(3)
		print("User:- ",str(inp))
		if str(inp) == '':
			speak('I think there is a problem in the microphone. Try to type please...')
			u = input('User:- ')
			main(u)
		else:
			main(str(inp))


def start_up():
	hour = int(time.strftime('%H'))
	tm = time.strftime('%I : %M %p')
	if hour <= 12:
		out = f'Good morning sir, Its {tm}. How can I help you?'
		speak(out)
		print(f'Ghost:- {out}')
	elif hour >= 12 and hour <= 17:
		out = f'Good afternoon sir, Its {tm}. How can I help you?'
		speak(out)
		print(f'Ghost:- {out}')
	elif hour >=17 and hour <= 20:
		out = f'Good evening sir, Its {tm}. How can I help you?'
		speak(out)
		print(f'Ghost:- {out}')
	else:
		out = f'Welcome sir, Its {tm}. How can I help you?'
		speak(out)
		print(f'Ghost:- {out}')


def main(u):
	u = u.lower()
	if u == 'exit':
		str = 'Bye sir, have a good day'
		speak(str)
		print(f'Ghost:- {str}')
		quit()
	elif u == 'quit':
		str = 'Bye sir, have a good day'
		speak(str)
		print(f'Ghost:- {str}')
		quit()
	elif 'say ' in u:
		extra, u = u.split('say ')
		speak(u)
		print(f'Ghost:- {u}')
	elif ' my ip' in u:
		ip = requests.get("https://api.ipify.org").text
		out = f'Your IP address is {ip}'
		speak(out)
		print(f'Ghost:- {out}')
	elif ' the time' in u:
		tim = time.strftime('%I : %M %p')
		out = f'The time is {tim}'
		speak(out)
		print(f'Ghost:- {out}')
	elif u == 'clear screen':
		os.system('clear')
	elif u == 'torch on':
		speak('turning torch on...')
		os.system('termux-torch on')
	elif u == 'torch off':
		speak('turning torch off...')
		os.system('termux-torch off')
	elif u == 'open youtube':
		speak('opening youtube...')
		os.system('termux-open-url https://m.youtube.com')
		quit()
	elif u == 'open stack overflow':
		speak('opening stackoverflow...')
		os.system('termux-open-url https://www.stackoverflow.com')
		quit()
	elif 'read pdf' in u:
		speak('Type the page number...')
		n = int(input('Ghost:- Type the page number:- '))
		readPDF(n)
	elif 'who is ' in u:
		extra, u = u.split('who is ')
		o = db.who.get(u, 'fls')
		if o == 'fls':
			try:
				speak('searching on wikipedia...')
				result = wikipedia.summary(u.upper(), sentences=1)
				out = f"According to wikipedia, {result}"
				speak(out)
				print(f'Ghost:- {out}')
			except:
				os.system('clear')
				out = f'\'{u.upper()}\' is not available in wikipedia. Try another keyword'
				speak(out)
				print(f'Ghost:- {out}')
		else:
			speak(o)
			print(f'Ghost:- {o}')
	else:
		out = db.qna.get(u, 'Sorry, I am learning')
		speak(out)
		print(f'Ghost:- {out}')


start_up()
take_input()
