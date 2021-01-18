import re
text = 'The ghost that syas boo baunts the loo'

ptn = re.compile(r'.oo')
print(re.findall(ptn, text))
