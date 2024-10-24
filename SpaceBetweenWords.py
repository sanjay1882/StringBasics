
import re
input="BruceWayneIsBatman"
words = re.findall('[A-Z][a-z]*', input) 
for i in words:
    print(i,end=' ')
