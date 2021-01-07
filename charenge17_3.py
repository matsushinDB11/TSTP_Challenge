import re
text = 'The ghost that syas boo baunts the loo'

ptn = re.compile(r'oo$')
if ptn.search(text):
    print('match')
else:
    print('no match')
# print(ptn.search(text).group(0))
