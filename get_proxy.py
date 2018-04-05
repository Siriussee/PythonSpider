import json
import urllib2
import re
import time

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


url = 'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html_text = response.read()
except:
    print 'error'

proxys = html_text.split('\n')
# '{"country": "TH", "response_time": 8.72, "anonymity": "high_anonymous", "export_address": ["61.91.235.226"], "host": "61.91.235.226", "type": "https", "port": 8080, "from": "txt"}'
# print proxys

proxys_plain = []
for proxy in proxys:
    try:
        text = json.loads(proxy, object_hook=JSONObject)
        # print text
        line = text.host + ':' + str(text.port)
        proxys_plain.append(line)
    except:
        continue



for proxy in proxys_plain:
    try:
        proxy_obj = urllib2.ProxyHandler({'http': proxy})
        opener = urllib2.build_opener(proxy_obj)
        urllib2.install_opener(opener)
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request, timeout = 5)
    except:
        try:print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' error ' + proxy + '\n'
        except:pass
        continue
    with open('proxy_2.txt', 'ab') as f:
        try:print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' pass ' + proxy + '\n'
        except:pass
        f.write(proxy + '\n')
