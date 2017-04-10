import requests
import json
base_url = 'http://www.btis.in/bcity_issues_transport.txt'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36"}
html = requests.get(base_url,headers=headers)
htmltext = html.text
data = json.loads(htmltext)
length_data = len(data)
for i in range(0,length_data):
    print data[i]['user']['name']
    print data[i]['issue_no']
    print data[i]['topic_id']
    print data[i]['title']
    print data[i]['status']
    print data[i]['topic_name']
    print data[i]['issue_type_name']
    print data[i]['comments']
    print data[i]['image_url']
    print data[i]['agency_name']
    print data[i]['created_at']
    print data[i]['issue_type_id']
    print data[i]['source']
    print data[i]['desc']
    print data[i]['id']
    print data[i]['ward_name']
    print data[i]['agency_id']
print length_data
