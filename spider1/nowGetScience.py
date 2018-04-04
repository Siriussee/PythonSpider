import urllib2

target = 'http://science.sciencemag.org/content/359/6372/199/tab-article-info'

# avoid exceptions
try:
    response = urllib2.urlopen(target)
except urllib2.URLError, e:
    print e.reason

f = open('test.html', 'w')

# write to file & local test
# wirte func is trunc in py2.7 by defalt
f.write(response.read())
f.close()