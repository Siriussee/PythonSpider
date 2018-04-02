import json
import urllib2
import re
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
except urllib2.URLError, e:
    print e.reason

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

work_proxys_plain = []

for proxy in proxys_plain:
    try:
        requests.get('http://science.sciencemag.org/content/339/6115/43/tab-article-info',proxies={"http": "http://" + proxy}, timeout=2)
    except:
        continue
    else:
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=http://' + proxy)
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--ignore-ssl-errors')
            browser = webdriver.Chrome(chrome_options=chrome_options)
            browser.set_page_load_timeout(30)
            browser.get('http://science.sciencemag.org/content/339/6115/43/tab-article-info')
            element = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.ID, "_altmetric_popover_el"))
            )
        except:
            try:print 'failed'
            except:pass
            browser.close()
            continue
        else:
            try:print 'good'
            except:pass
            work_proxys_plain.append(proxy)
            with open('good_proxy_2.txt', 'ab') as f:
                f.write(proxy+'\n')
        browser.close()

with open('proxy.txt', 'ab') as f:
    for proxy in work_proxys_plain:
        f.write(proxy+'\n')
