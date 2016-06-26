import requests
from bs4 import BeautifulSoup
import sys

"""
This request is from http://www.deccanherald.com/contents/256/point-blank-bengaluru.html
"""

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36"}

def request_call(index):
	url = 'http://www.deccanherald.com/more_category_news.php?page='+str(index)+'&cid=256'
	htmltext = requests.get(url,headers=headers).text
	soup =  BeautifulSoup(htmltext,'lxml')
	result = soup.findAll('div',{'class':'categoryNewsText'})
	for res in range(0,len(result)): 
		get_h2(result[res])
		get_div(result[res])
		get_p(result[res])
		print "+++++++++++++++++++++++"

def get_h2(tagObject):
	print tagObject.h2.getText()
	print tagObject.h2.a['href']

def get_div(tagObject):
	print tagObject.div.i.findNextSibling().contents[0]

def get_p(tagObject):
	print tagObject.p.getText()


lst = [ind for ind in range(0,50)]
[request_call(num) for num in lst]