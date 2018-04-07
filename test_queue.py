import Queue
import urllib2
import re
import time 
import random

q = Queue.Queue()

with open('url_of_papers_no_404.txt', 'r') as f:
    urls = f.read().split('\n')

with open('proxy_2.txt', 'r') as f:
    proxys = f.read().split('\n')

for url in urls:
    q.put(url)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

while q.qsize() > 20:
    url = q.get()
    try:
        index = random.randint(0,len(proxys)-2)
        random_proxy = proxys[index]

        try:print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +' getting ' + url + ' finished [' + str(10134 - q.qsize()) + '/10134]'
        except:pass
    
        proxy_obj = urllib2.ProxyHandler({'http': random_proxy})
        opener = urllib2.build_opener(proxy_obj)
        urllib2.install_opener(opener)
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request, timeout = 5)
        html_text = response.read()
    except:
        q.put(url)
        try:print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +' timeout ' + url + ' leaving '+ str(len(proxys)-1)
        except:pass
        if len(proxys)-2 > 80:
            del proxys[index]
        continue

    try:
        pattern_mata_data = re.compile(r'<div class="meta-line">.*?</div>',re.S)
        mata_data = re.findall(pattern_mata_data,html_text)[0]

        pattern_DOI = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)\b')
        DOI = re.findall(pattern_DOI,mata_data)[0]
    except:
        q.put(url)
        try:print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +' fail to read ' + url
        except:pass
        continue

    # match article category
    # <div class="overline">Reports</div>
    # <div class="overline"><span class="overline__section">News & Analysis</span></div>
    pattern_catagory = re.compile(r'<div class="overline">.*?</div>',re.S)
    catagory = re.findall(pattern_catagory,html_text)[0].split('>')[1].split('<')[0] if re.findall(pattern_catagory,html_text) else ''
    if catagory.strip() == '':
        pattern_catagory_in_lines = re.compile(r'<span class="overline__section">.*?</span>',re.S)
        catagory = re.findall(pattern_catagory_in_lines,html_text)[0].split('>')[1].split('<')[0] if re.findall(pattern_catagory_in_lines,html_text) else 'null'
    # print catagory

    with open('API_url_9.txt', 'ab') as f:
        f.write('https://api.altmetric.com/v1/doi/'+ DOI + '#' + catagory +'\n')

while not q.empty():
    with open('error_urls.txt', 'ab') as f:
        f.write(q.get() +'\n')