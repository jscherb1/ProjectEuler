from collections import defaultdict
from math import sqrt

def factor(n):
    i = 2
    limit = sqrt(n)    
    while i <= limit:
      if n % i == 0:
        yield i
        n = n / i
        limit = sqrt(n)   
      else:
        i += 1
    if n > 1:
        yield n

num = 644
d=defaultdict(int)
for f in factor(num):
    d[f]+=1

terms=[]
base = sorted(d.keys())
for e in base:
    if e>1:
        #terms.append('{:,}^{}'.format(e,d[e]))
        terms.append(e**d[e])

    #else:
        #terms.append('{:,}'.format(e))
        #terms.appendd(e**d[e])
    #result = ' * '.join(terms),'=','{:,}'.format(num) 

print(terms)


