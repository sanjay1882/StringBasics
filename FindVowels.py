s="EvenApple"
a=s.lower()
d={'a','e','i','o','u'}
Vowels=0
Constants=0
for i in range(len(a)):
    if a[i] in d:
        Vowels+=1
    else:
        Constants+=1
print("Vowels:",Vowels,"Constants :",Constants)
