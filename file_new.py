import random
random.seed(13)
a= [random.randint(1,15) for i in range(25)]
print(a)

for el in a:
     for j in range(len(a)-1):
          if a[j]>a[j+1]:
               a[j],a[j+1]=a[j+1],a[j]




print(a)