#coding=utf-8

from selenium import webdriver
import re
import time
import csv  
import numpy
import random

file_name = time.strftime("%Y%m%d") + '_Science_statistic.csv'

with open(file_name, 'wb') as file:
    writer = csv.writer(file)
    first_list = ['DOI','catagory','pubilcation date','title','altmetric score','outlets','blogged','tweeted','facebooked','google+','wikipedia','videoed','reddited','mendeleyed']
    writer.writerow(first_list)

with open('url_of_papers.txt', 'r') as f:
    urls = f.read().split('\n')

with open('good_proxy.txt', 'r') as f:
    proxys = f.read().split('\n')

time_out_urls = []
for url in urls:
    try:
        chrome_options = webdriver.ChromeOptions()
        random_proxy = proxys[random.randint(0,20)]
        print 'using ' + random_proxy
        chrome_options.add_argument('--proxy-server=http://' + random_proxy)
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.set_page_load_timeout(60)
        browser.get(url)
    except:
        # print 'a page is time out'
        time_out_urls.append(url)
        browser.close()
        continue
    html_text=browser.page_source
    time.sleep(1)
    browser.close()
    # print html_text # full element of science page

    # match altmetric_score
    pattern_altmetric_score = re.compile(r'alt="Article has an altmetric score of \d+')

    #check not found page
    if len(re.findall(pattern_altmetric_score,html_text)) == 0:
        continue

    altmetric_score = re.findall(pattern_altmetric_score,html_text)[0].split(' ')[6]
    # print altmetric_score

    # Picked up by <b>162</b> news outlets
    pattern_outlet = re.compile(r'Picked up by <b>\d+</b> news outlets')
    outlets = re.findall(pattern_outlet,html_text)[0].split('<b>')[1].split('</b>')[0] if re.findall(pattern_outlet,html_text) else '0'
    # print outlets

    # Blogged by <b>24</b>
    pattern_blogged = re.compile(r'Blogged by <b>\d+</b>')
    blogged = re.findall(pattern_blogged,html_text)[0].split('<b>')[1].split('</b>')[0] if re.findall(pattern_blogged,html_text) else '0'
    # print blogged

    # Tweeted by <b>260</b>
    pattern_tweet = re.compile(r'Tweeted by <b>\d+</b>')
    tweeted = re.findall(pattern_tweet,html_text)[0].split('<b>')[1].split('</b>')[0] if re.findall(pattern_tweet,html_text) else '0'
    # print tweeted

    # On <b>13</b> Facebook pages
    pattern_facebook = re.compile(r'On <b>\d+</b> Facebook pages')
    facebooked = re.findall(pattern_facebook,html_text)[0].split('<b>')[1].split('</b>')[0] if re.findall(pattern_facebook,html_text) else '0'
    # print facebooked

    # Referenced in <b>7</b> Wikipedia pages
    pattern_wiki = re.compile(r'Referenced in <b>\d+</b> Wikipedia pages')
    wikied = re.findall(pattern_wiki,html_text)[0].split('<b>')[1].split('</b>')[0] if re.findall(pattern_wiki,html_text) else '0'
    # print wikied

    # Mentioned in <b>8</b> Google+ posts
    pattern_gplus =re.compile(r'Mentioned in <b>\d+</b>')
    gplus = re.findall(pattern_gplus,html_text)[0].split('<b>')[1].split('</b>')[0] if re.findall(pattern_gplus,html_text) else '0'
    # print gplus

    # Reddited by <b>1</b>
    pattern_reddit = re.compile(r'Reddited by <b>\d+</b>')
    reddited = re.findall(pattern_reddit,html_text)[0].split('<b>')[1].split('</b>')[0] if re.findall(pattern_reddit,html_text) else '0'
    # print reddited

    # On <b>2</b> videos
    pattern_vedio = re.compile(r'On <b>\d+</b> videos')
    videoed = re.findall(pattern_vedio,html_text)[0].split('<b>')[1].split('</b>')[0] if re.findall(pattern_vedio,html_text) else '0'
    # print videoed

    # <b>44</b> readers on Mendeley
    pattern_mendeley = re.compile(r'<b>\d+</b> readers on Mendeley')
    mendeleyed = re.findall(pattern_mendeley,html_text)[0].split('<b>')[1].split('</b>')[0] if re.findall(pattern_mendeley,html_text) else '0'
    # print mendeleyed

    pattern_mata_data = re.compile(r'<div class="meta-line">.*?</div>',re.S)
    mata_data = re.findall(pattern_mata_data,html_text)[0]
    #print mata_data

    pattern_DOI = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)\b')
    DOI = re.findall(pattern_DOI,mata_data)[0]
    # print DOI

    # match article category
    # <div class="overline">Reports</div>
    # <div class="overline"><span class="overline__section">News & Analysis</span></div>
    pattern_catagory = re.compile(r'<div class="overline">.*?</div>',re.S)
    catagory = re.findall(pattern_catagory,html_text)[0].split('>')[1].split('<')[0]
    if catagory.strip() == '':
        pattern_catagory_in_lines = re.compile(r'<span class="overline__section">.*?</span>',re.S)
        catagory = re.findall(pattern_catagory_in_lines,html_text)[0].split('>')[1].split('<')[0]
    # print catagory

    # match article title
    # <h1 class="article__headline"><div class="highwire-cite-title">Exposed subsurface ice sheets in the Martian mid-latitudes</div></h1>
    pattern_title = re.compile(r'<h1 class="article__headline">.*</h1>')
    title = re.findall(pattern_title,html_text)[0].split('>')[2].split('<')[0]
    # print title

    # match pubilcation date
    # <div class="meta-line"><cite>Science&nbsp;</cite> 12 Jan 2018:<br />Vol. 359, Issue 6372, pp. 199-201<br />DOI: 10.1126/science.aao1619</div>
    pattern_pubilcation_date = re.compile(r'</cite> .*:<br />')
    pubilcation_date = re.findall(pattern_pubilcation_date,mata_data)[0].split('>')[1].split(':')[0][1:]
    # print pubilcation_date

    data_list = [DOI,catagory,pubilcation_date,title.encode('UTF-8'),altmetric_score,outlets,blogged,tweeted,facebooked,gplus,wikied,videoed,reddited,mendeleyed]
    # file = open(file_name,'wb')
    with open(file_name, 'ab') as file:
        writer = csv.writer(file)
        writer.writerow(data_list)

browser.quit()

with open('skipped_url.txt', 'wb') as f:
    for url in time_out_urls:
        f.write(url+'\n')