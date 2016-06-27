'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : getting data from deccan herald .

Description:
This request is from http://www.deccanherald.com/contents/256/point-blank-bengaluru.html. Using a request made inside the deccan herald page to extract data related
with civic issues.

'''
import requests
from bs4 import BeautifulSoup
import sys
from nltk.tokenize import sent_tokenize,word_tokenize


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36"}

all_data = []
key_words = ['roads','road','BBMP','bus','buses','street','traffic','stagnation']

def request_call(index):
	url = 'http://www.deccanherald.com/more_category_news.php?page='+str(index)+'&cid=256'
	htmltext = requests.get(url,headers=headers).text
	soup =  BeautifulSoup(htmltext,'lxml')
	result = soup.findAll('div',{'class':'categoryNewsText'})
	print url
	print '\n\n\n\n'
	for res in range(0,len(result)):
		insert_dict(result[res].h2.a['href'],result[res].h2.getText(),result[res].div.i.findNextSibling().contents[0],result[res].p.getText())
		#print result[res].h2.getText()
		#print result[res].h2.a['href']
		#print result[res].div.i.findNextSibling().contents[0]
		#print result[res].p.getText()

def insert_dict(text_link,text_title,text_date,text_description):
	dictionary = {'link':'','title':'','date':'','description':''}
	dictionary['link'] = 'http://www.deccanherald.com' + text_link
	dictionary['title'] = text_title
	dictionary['date'] = text_date
	dictionary['description'] = text_description
	all_data.append(dictionary)
	print all_data


lst = [ind for ind in range(0,50)]
[request_call(num) for num in lst]

file = open('data1.txt','a')

for index in range(0,len(all_data)):
	if(len( set(word_tokenize(all_data[index]['description'])) & set(key_words)) > 0):
		all_data[index]['description'] = all_data[index]['description'].encode('ascii', 'ignore')
		all_data[index]['title'] = all_data[index]['title'].encode('ascii', 'ignore')
		all_data[index]['date'] = all_data[index]['date'].encode('ascii', 'ignore')
		all_data[index]['link'] = all_data[index]['link'].encode('ascii', 'ignore')
		file.write(all_data[index]['title'])
		file.write('\n')
		file.write(all_data[index]['description'])
		file.write('\n')
		file.write(all_data[index]['date'])
		file.write('\n')
		file.write(all_data[index]['link'])
		file.write('\n')

file.close()


'''
def get_h2(tagObject):
	print tagObject.h2.getText()
	print tagObject.h2.a['href']

def get_div(tagObject):
	print tagObject.div.i.findNextSibling().contents[0]

def get_p(tagObject):
	print tagObject.p.getText()
'''
