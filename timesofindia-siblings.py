'''
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : getting data from times of india .

Description:
Using a request made inside the page of the newspaper times of india to get news related with bangalore
and using python libraries to extract that data.

'''
from nltk.tokenize import sent_tokenize,word_tokenize
import requests
from bs4 import BeautifulSoup
import re

all_data = []
key_words = ['roads','road','BBMP','bus','buses','street','traffic','stagnation']
#url = 'http://timesofindia.indiatimes.com/articlelist_lazyload/-2128833038.cms?curpg='+str(index)
def request_page(url):	
	html = requests.get(url)
	htmltext = html.text
	extract_data(htmltext)

def insert_dict(text_by,text_link,text_title,text_date):
	dictionary = {'by':'','link':'','title':'','date':''}
	dictionary['by'] = text_by
	dictionary['link'] = 'http://timesofindia.indiatimes.com' + text_link
	dictionary['title'] = text_title
	dictionary['date'] = text_date
	all_data.append(dictionary)


def extract_data(htmltext):
	soup = BeautifulSoup(htmltext,'lxml')
	written_by = soup.findAll('span',attrs={'class':'bln'})
	
	for tag in written_by: 
		insert_dict(tag.getText(),tag.previous_sibling.a['href'],tag.previous_sibling.getText(),tag.find('span')['rodate'])


for index in range(1,12):
	url = 'http://timesofindia.indiatimes.com/articlelist_lazyload/-2128833038.cms?curpg='+str(index)
	request_page(url)
print all_data

file = open('data.txt','a')

for index in range(0,len(all_data)):
	if(len( set(word_tokenize(all_data[index]['title'])) & set(key_words)) > 0):
		all_data[index]['title'] = all_data[index]['title'].encode('ascii', 'ignore')
		file.write(all_data[index]['title'])
		file.write('\n')
		file.write(all_data[index]['by'])
		file.write('\n')
		file.write(all_data[index]['date'])
		file.write('\n')
		file.write(all_data[index]['link'])
		file.write('\n')

file.close()
"""
USE THESE COMMENTS IF NEEDED


#text_by = tag.getText()
		#text_link =  tag.previous_sibling.a['href']
		#text_title = tag.previous_sibling.getText()
		#insert_dict(text_by,text_link,text_title)
"""