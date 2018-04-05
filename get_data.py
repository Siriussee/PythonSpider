import urllib2
import re
import json
import csv 
import time

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

file_name = time.strftime("%Y%m%d") + '_Science_statistic.csv'

first_list = [
        'catagory','title','doi',
        'published date','Altmetric score',
        'Score change in 1 year','Score change in 6 months','Score change in 3 months','Score change in 1 months',
        'Score change in 1 week','Score change in 5d','Score change in 3d','Score change in 1d',
        'readers count','Shared on Facebook','Mentionded in blogs',
        'Shared on G+','Mentionded in news','Number of discreet mentions',
        'Reddit posts','Tweeted','Number of the Youtube/Vimeo channels',
    ]

with open(file_name, 'wb') as file:
    writer = csv.writer(file)
    writer.writerow(first_list)

with open('API_url_2.txt', 'r') as f:
    datas = f.read().split('\n')

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

for data in datas:
    url = data.split('#')[0]
    catagory = data.split('#')[1]
    try:
        time.sleep(1)
        try:print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'getting ' + url 
        except:pass
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request, timeout = 10)
        # print response.read()
        html_text = response.read()
        data = json.loads(html_text)
    except:
       with open('log2.txt', 'ab') as f:
            f.write(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 
                ' an error occurred when requesting *' + url
            )
        continue

    

    if not data.has_key('cited_by_fbwalls_count'):
        data['cited_by_fbwalls_count'] = 0
    if not data.has_key('cited_by_tweters_count'):
        data['cited_by_tweters_count'] = 0
    if not data.has_key('cited_by_feeds_count'):
        data['cited_by_feeds_count'] = 0
    if not data.has_key('cited_by_gplus_count'):
        data['cited_by_gplus_count'] = 0
    if not data.has_key('cited_by_msm_count'):
        data['cited_by_msm_count'] = 0
    if not data.has_key('cited_by_posts_count'):
        data['cited_by_posts_count'] = 0
    if not data.has_key('cited_by_rdts_count'):
        data['cited_by_rdts_count'] = 0
    if not data.has_key('cited_by_tweeters_count'):
        data['cited_by_tweeters_count'] = 0
    if not data.has_key('cited_by_videos_count'):
        data['cited_by_videos_count'] = 0

    data_list = [
        catagory,data['title'].encode('UTF-8'),data['doi'],
        time.strftime("%Y-%m-%d",time.localtime(data['published_on'])),data['score'],
        data['history']['1y'],data['history']['6m'],data['history']['3m'],data['history']['1m'],
        data['history']['1w'],data['history']['5d'],data['history']['3d'],data['history']['1d'],
        data['readers_count'],data['cited_by_fbwalls_count'],data['cited_by_feeds_count'],
        data['cited_by_gplus_count'],data['cited_by_msm_count'],data['cited_by_posts_count'],
        data['cited_by_rdts_count'],data['cited_by_tweeters_count'],data['cited_by_videos_count'],
    ]

    with open(file_name, 'ab') as file:
        writer = csv.writer(file)
        writer.writerow(data_list)
