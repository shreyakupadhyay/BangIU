import requests
from bs4 import BeautifulSoup
import re

#for i in range(1,12):
all_data = []

#url = 'http://timesofindia.indiatimes.com/articlelist_lazyload/-2128833038.cms?curpg='+str(index)
def request_page(url):	
	html = requests.get(url)
	htmltext = html.text
	get_data_soup(htmltext)

def insert_dict(text_by,text_link,text_title,text_date):
	dictionary = {'by':'','link':'','title':'','date':''}
	dictionary['by'] = text_by
	dictionary['link'] = 'http://timesofindia.indiatimes.com' + text_link
	dictionary['title'] = text_title
	dictionary['date'] = text_date
	all_data.append(dictionary)


def get_data_soup(htmltext):
	soup = BeautifulSoup(htmltext,'lxml')
	written_by = soup.findAll('span',attrs={'class':'bln'})
	
	for tag in written_by: 
		insert_dict(tag.getText(),tag.previous_sibling.a['href'],tag.previous_sibling.getText(),tag.find('span')['rodate'])

def go_link(text_link):
	request_page(text_link)


for index in range(1,12):
	url = 'http://timesofindia.indiatimes.com/articlelist_lazyload/-2128833038.cms?curpg='+str(index)
	request_page(url)
print all_data

"""
USE THESE COMMENTS IF NEEDED


#text_by = tag.getText()
		#text_link =  tag.previous_sibling.a['href']
		#text_title = tag.previous_sibling.getText()
		#insert_dict(text_by,text_link,text_title)
"""