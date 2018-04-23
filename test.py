import re

aaa = '[-4]'

print(aaa)

# aaa = str.replace(aaa, '[', '')
# aaa = str.replace(aaa, ']', '')
aaa = re.sub('[\[\]]', '', aaa)

bbb = int(aaa)
print(bbb)
