import requests
import jsbeautifier
import json
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36"}
"""
from 0 to 10 and when using 10 date is 2015-11-17
So for last 6 months issues use upto 10
"""
base_url = 'http://www.ichangemycity.com/card/get_complaints/2?agency=0&category_id=0&lat=12.9715987&lon=77.59456269999998&status_id=0&sub_category=67'
html = requests.get(base_url,headers = headers)
htmltext = html.text
res = jsbeautifier.beautify(htmltext)
data = json.loads(htmltext)
print data['status']
length_result = len(data['result'])
print length_result
for i in range(0,length_result):
    print data['result'][i]['complaint_created']
    print data['result'][i]['complaint_title']
    print data['result'][i]['complaint_description']
    print data['result'][i]['complaint_location']
    print data['result'][i]['complaint_address_1']
    print data['result'][i]['category_name']
    print data['result'][i]['ward_name']
    print data['result'][i]['complaint_source_id']
    print data['result'][i]['civic_agency_name']
#print res
