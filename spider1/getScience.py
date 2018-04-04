import urllib2
import re

url = 'http://science.sciencemag.org/content/359/6372/199/tab-article-info'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    # print response.read()
except urllib2.URLError, e:
    print e.reason

pattern_altmetric_core = re.compile(r'alt="Article has an altmetric score of \d+')

content = response.read()
items = re.findall(pattern_altmetric_core,content)

print items


'''
f = open('test.html', 'w')

# write to file & local test
# wirte func is trunc in py2.7 by defalt
f.write(response.read())
f.close()

'''