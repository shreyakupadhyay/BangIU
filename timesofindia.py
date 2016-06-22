import requests
import re
for i in range(1,12):
    url = 'http://timesofindia.indiatimes.com/articlelist_lazyload/-2128833038.cms?curpg='+str(i)
    html = requests.get(url)
    htmltext = html.text
    regex = re.escape('<a hid="')+'(.+?)'+re.escape('" pg="" href="')+'(.+?)'+re.escape('">')+'(.+?)'+re.escape('</a>')
    regex_time = re.escape('<span style="color:#92A1A7;font-family:arial;font-size:11px;" id="')+'(.+?)'+re.escape('" rodate="')+'(.+?)'+re.escape('"></span>')
    pattern = re.compile(regex)
    pattern_time = re.compile(regex_time)
    result = re.findall(pattern,htmltext)
    result_time = re.findall(pattern_time,htmltext)
    print result,len(result)
    print '\n\n'
    print result_time,len(result_time)
    print '\n\n\n'
