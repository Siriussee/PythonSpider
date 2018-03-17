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