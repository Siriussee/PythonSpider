import urllib2
import re
import json
import csv 
import time

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

file_name = time.strftime("%Y%m%d") + '_Science_statistic.csv'

with open('API_url_2.txt', 'r') as f:
    datas = f.read().split('\n')

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

for data in datas:
    url = data.split('#')[0]
    catagory = data.split('#')[1]
    try:
        time.sleep(1)
        try:print 'getting ' + url 
        except:pass
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
        # print response.read()
    except urllib2.URLError, e:
        print e.reason

    html_text = response.read()
    data = json.loads(html_text, object_hook=JSONObject)
    if not data.cited_by_fbwalls_count:
        data.cited_by_fbwalls_count = 65535
    print data.cited_by_fbwalls_count

'''
    # print data.history

    if not data.has_key('cited_by_fbwalls_count'):
        data.cited_by_fbwalls_count = 0
    if not data.has_key('cited_by_tweters_count'):
        data.cited_by_tweters_count = 0
    if not data.has_key('cited_by_accounts_count'):
        data.cited_by_accounts_count = 0

    data_list = [catagory,data.title,data.doi,data.published_on, 
    data.score, 
    data.cited_by_fbwalls_count,data.cited_by_tweters_count,data.cited_by_accounts_count, 
    data.readers_count]

    print data['title']
    # data_list = [catagory,data['title'],data['doi'],data['published_on'],data['score'],data['history']['1y']]

    with open(file_name, 'ab') as file:
        writer = csv.writer(file)
        writer.writerow(data_list)

    '''

