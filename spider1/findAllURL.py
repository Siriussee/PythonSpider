from selenium import webdriver
import re
import time
import numpy
import urllib2
import random

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
        time.sleep(random.randint(2,5))
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

# print contents

for content in contents:
    request = urllib2.Request(content, headers = headers)
    response = urllib2.urlopen(request)
    html_text = response.read()
    time.sleep(random.randint(2,5))
    print content + ' is searched'
    # href="/content/341/6145/476"
    pattern_url_in_list = re.compile(r'/content/\d+/\d+/\d+')
    papers = re.findall(pattern_url_in_list,html_text)
    unique_papers = numpy.unique(papers);

    # url_of_papers = []
    f = open('url_of_papers.txt', 'a')

    for paper in unique_papers:
        paper_line = 'http://science.sciencemag.org' + paper + '/tab-article-info\n' 
        # url_of_papers.append(paper_line)
        f.write(paper_line)

    f.close()

