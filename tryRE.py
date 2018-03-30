import re

# genarate pattern via (string)
# re.compile('pattern', re.I | re.M), you can set mode like re.I
pattern = re.compile(r'hello')
 
# use pattern to match (string)
match = pattern.match('hello world!')
print match.group()
 
# or you can just do
m = re.match(r'hello', 'hello world!')
# without pattern
print m.group()

# if is not in the beginning of string
# match = pattern.match('world! hello~')
# print match.group()
# return NoneType error

# should use search(string)
match = pattern.search('world! hello~')
print match.group()
# works!

# test spilt
pattern = re.compile(r'\d+')
print re.split(pattern,'one1two2three3four4')
# ['one', 'two', 'three', 'four', '']

# test findall
pattern = re.compile(r'\d+')
print re.findall(pattern,'one1two2three3four4')
# ['1', '2', '3', '4']


pattern = re.compile(r'\d+')
print re.findall(pattern,'65535qwe12345')

pattern_altmetric_core = re.compile(r'alt="Article has an altmetric score of \d+')
print re.findall(pattern_altmetric_core,'<img alt="Article has an altmetric score of 1665">')

pattern_DOI = re.compile(r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)\b')
print re.findall(pattern_DOI,'href="https://doi.org/10.1126/science.aao1619" link_ta')

pattern_title = re.compile(r'<h1 class="article__headline">.*</h1>')
print re.findall(pattern_title,'<h1 class="article__headline"><div class="highwire-cite-title">Exposed subsurface ice sheets in the Martian mid-latitudes</div></h1>')

pattern_pubilcation_date = re.compile(r'<div class="meta-line">.*</div>')
print re.findall(pattern_pubilcation_date,'<div class="meta-line"><cite>Science&nbsp;</cite> 12 Jan 2018:<br />Vol. 359, Issue 6372, pp. 199-201<br />DOI: 10.1126/science.aao1619</div>')


pattern_mata_data = re.compile(r'<cite> Science </cite>.*</div>')
mata_data = re.findall(pattern_mata_data,'<cite>Science </cite> 12 Jan 2018:<br />Vol. 359, Issue 6372, pp. 199-201<br />DOI: 10.1126/science.aao1619      </div>')
print mata_data

pattern_url_by_day = re.compile(r'/content/\d+/\d+')
print re.findall(pattern_url_by_day,'<div class="highwire-cite-highlight"><a href="/content/339/6115"')


pattern_outlet = re.compile(r'Picked up by <b>\d+</b> news outlets')
print re.findall(pattern_outlet,'error')[0].split('<b>')[1].split('</b>')[0] if re.findall(pattern_outlet,'error') else '0'


    # <div class="overline">Reports</div>
    # <div class="overline"><span class="overline__section">News & Analysis</span></div>
pattern_catagory = re.compile(r'<div class="overline">.*?</div>',re.S)
catagory = re.findall(pattern_catagory,'<div class="overline">Reports</div>')[0].split('>')[1].split('<')[0]
if catagory.strip() == '':
    pattern_catagory_in_lines = re.compile(r'<span class="overline__section">.*</span>')
    catagory = re.findall(pattern_catagory_in_lines,'<div class="overline">Reports</div>')[0].split('>')[1].split('<')[0]
print catagory

pattern_catagory = re.compile(r'<div class="overline">.*?</div>',re.S)
catagory = re.findall(pattern_catagory,'<div class="overline">\n<span class="overline__section">News & Analysis</span>\n</div>')[0].split('>')[1].split('<')[0]
if catagory.strip() == '':
    pattern_catagory_in_lines = re.compile(r'<span class="overline__section">.*</span>')
    catagory = re.findall(pattern_catagory_in_lines,'<div class="overline">\n<span class="overline__section">News & Analysis</span>\n</div>')[0].split('>')[1].split('<')[0]
print catagory
