from selenium import webdriver
import re
import time

# url = 'http://science.sciencemag.org/content/359/6372/199/tab-article-info'

url_by_year = 'http://science.sciencemag.org/content/by/year/2013'
browser = webdriver.Chrome()
browser.get(url_by_year)
html_text=browser.page_source
browser.close()

'''
f = open('2013-archive.html', 'w')
f.write(html_text.encode('utf-8'))
f.close()
'''

#  <div class="highwire-cite-highlight"><a href="/content/339/6115" class="highlight-image-linked"><img class="highlight-image" src="https://d2ufo47lrtsv5s.cloudfront.net/sites/default/files/styles/sci_issue_archive_cover/public/highwire/sci/339/6115.cover-source.gif?itok=pGqLLXf8" alt="Science: 339 (6115)" /></a></div>
