import urllib2
import re
import time

url = 'http://science.sciencemag.org/content/339/6115/14/tab-article-info'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

with open('url_of_papers.txt', 'r') as f:
    urls = f.read().split('\n')

urls_no_404 = []

for url in urls:
    try:
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
        # print response.read()
        time.sleep(0.5)
        urls_no_404.append(url)
    except:
        try:
            print "kill " + url
        except: pass
        continue

with open('url_of_papers_no_404.txt', 'wb') as f:
    for url in urls_no_404:
        f.write(url+'\n')
