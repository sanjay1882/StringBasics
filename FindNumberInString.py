
import re
input="BruceWayneIs2ww242Batman"
words = re.findall('\d', input) 
for i in words:
    print(i,end=' ')
