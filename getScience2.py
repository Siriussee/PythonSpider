from selenium import webdriver
import re

url = 'http://science.sciencemag.org/content/359/6372/199/tab-article-info'

browser = webdriver.Chrome()
browser.get(url)
html_text=browser.page_source
# print html_text # full element of science page
'''
f = open('test.html', 'w')

# write to file & local test
# wirte func is trunc in py2.7 by defalt
f.write(html_text.encode('utf-8'))
f.close()
'''

# match altmetric_score
pattern_altmetric_score = re.compile(r'alt="Article has an altmetric score of \d+')
altmetric_score = re.findall(pattern_altmetric_score,html_text)

# Picked up by <b>162</b> news outlets

# Blogged by <b>24</b>

# Tweeted by <b>260</b>

# On <b>13</b> Facebook pages
# Referenced in <b>7</b> Wikipedia pages
# Mentioned in <b>8</b> Google+ posts
# Reddited by <b>1</b>
# On <b>2</b> videos
# <b>44</b> readers on Mendeley

# match DOI
# https://doi.org/10.1126/science.aao1619
pattern_DOI = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)\b')
# will find 2 of them
DOI = re.findall(pattern_DOI,html_text)

# match article category
# <header class="article__header"><div class="overline">Reports</div>

# match article title
# <h1 class="article__headline"><div class="highwire-cite-title">Exposed subsurface ice sheets in the Martian mid-latitudes</div></h1>
pattern_title = re.compile(r'<h1 class="article__headline">.*</h1>')
tltle = re.findall(pattern_title,html_text)

# match pubilcation date
# <div class="meta-line"><cite>Science&nbsp;</cite> 12 Jan 2018:<br />Vol. 359, Issue 6372, pp. 199-201<br />DOI: 10.1126/science.aao1619</div>
pattern_pubilcation_date = re.compile(r'<div class="meta-line">.*</div>')
pubilcation_date = re.findall(pattern_pubilcation_date,html_text)
