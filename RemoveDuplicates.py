a="programming"
d=set(a)
for i in a:
    if i in d:
        print(i,end='')
        d.remove(i)
