import PyPDF2
import os


def speak(text):
	os.system(f'termux-tts-speak \'{text}\'')


def readPDF(pageNum):
	file = open('sample.pdf', 'rb')
	reader = PyPDF2.PdfFileReader(file)
	page = reader.getPage(pageNum - 1)
	speak(page.extractText())
	print('Ghost:- PDF:- \n' + page.extractText())
