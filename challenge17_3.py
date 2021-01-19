import re
text = 'The ghost that syas boo baunts the loo'

ptn = re.compile(r'.o{2}')
print(re.findall(ptn, text))
