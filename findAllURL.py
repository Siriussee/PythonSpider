from selenium import webdriver
import re
import time
import numpy
import urllib2

# url = 'http://science.sciencemag.org/content/359/6372/199/tab-article-info'

urls_by_year = [
    'http://science.sciencemag.org/content/by/year/2013',
    'http://science.sciencemag.org/content/by/year/2014',
    'http://science.sciencemag.org/content/by/year/2015',
    'http://science.sciencemag.org/content/by/year/2016',
    'http://science.sciencemag.org/content/by/year/2017',
    'http://science.sciencemag.org/content/by/year/2018'
    ]

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

html_text = ''

try:
    for url_by_year in urls_by_year:
        request = urllib2.Request(url_by_year, headers = headers)
        response = urllib2.urlopen(request)
        html_text += response.read() + '\n'
        time.sleep(2)
        print url_by_year + ' is searched'
except urllib2.URLError, e:
    print e.reason

#  <div class="highwire-cite-highlight"><a href="/content/339/6115" 
pattern_url_by_day = re.compile(r'/content/\d+/\d+')
url_by_day = re.findall(pattern_url_by_day,html_text)
unique_url_by_day = numpy.unique(url_by_day);
# print url_by_day
# f = open('content_line.txt', 'w')

contents = []
for each in unique_url_by_day:
    content_line = 'http://science.sciencemag.org' + each
    contents.append(content_line)
    # f.write(content_line)

# print url_by_day

# f.close()

print contents