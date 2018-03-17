# will get all HTML code in baidu

import urllib2

# urlopen(url, data = None, timeout =  socket._GLOBAL_DEFAULT_TIMEOUT)
response = urllib2.urlopen("http://www.baidu.com")

# res - <addinfourl at 95873864L whose fp = <socket._fileobject object at 0x0000000005A705E8>
# res.read() - HTML
print response.read()