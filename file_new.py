import random
random.seed(12)
a= [random.randint(1,15) for i in range(25)]
print(a)

new=[]

while len(a)!=0:
    b=min(a)
    a.remove(b)
    if b not in new:
        new.append(b)

print(new)