import urllib
import urllib2
import re

url = 'https://www.qiushibaike.com/hot/page/2/'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    # print response.read()
except urllib2.URLError, e:
    print e.reason

content = response.read().decode('utf-8')
pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                    'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)

items = re.findall(pattern,content)
for item in items:
    print item[0],item[1],item[2],item[3],item[4]