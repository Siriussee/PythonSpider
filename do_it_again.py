import urllib2
import re
import time 

with open('url_of_papers_no_404.txt', 'r') as f:
    urls = f.read().split('\n')

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
for url in urls:
    try:
        try:print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +' getting ' + url 
        except:pass
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request, timeout = 10)
        # print response.read()
        html_text = response.read()
    except:
        with open('log.txt', 'ab') as f:
            f.write(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 
                ' an error occurred when requesting *' + url + '\n'
            )
        continue


    pattern_mata_data = re.compile(r'<div class="meta-line">.*?</div>',re.S)
    mata_data = re.findall(pattern_mata_data,html_text)[0]

    pattern_DOI = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)\b')
    DOI = re.findall(pattern_DOI,mata_data)[0]

    # match article category
    # <div class="overline">Reports</div>
    # <div class="overline"><span class="overline__section">News & Analysis</span></div>
    pattern_catagory = re.compile(r'<div class="overline">.*?</div>',re.S)
    catagory = re.findall(pattern_catagory,html_text)[0].split('>')[1].split('<')[0] if re.findall(pattern_catagory,html_text) else ''
    if catagory.strip() == '':
        pattern_catagory_in_lines = re.compile(r'<span class="overline__section">.*?</span>',re.S)
        catagory = re.findall(pattern_catagory_in_lines,html_text)[0].split('>')[1].split('<')[0] if re.findall(pattern_catagory_in_lines,html_text) else 'null'
    # print catagory

    with open('API_url_5.txt', 'ab') as f:
        f.write('https://api.altmetric.com/v1/doi/'+ DOI + '#' + catagory +'\n')

