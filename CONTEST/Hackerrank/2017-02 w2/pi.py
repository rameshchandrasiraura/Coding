import sys
import math

PI = 3.14159265358979323846264338327950288419716939993751
mn,mx = map(int,raw_input().split(' '))
diff,N,D= 1e20,1e20,1e20
for d in range(mn,mx+1):
    n1 = math.floor(d*PI)
    #print int(n1)
    if (abs(n1/d - PI)<diff):
        diff = abs(n1/d - PI)
        N,D = n1,d
    n2 = math.ceil(d*PI)
    #print int(n2)
    if (abs(n2/d - PI)<diff):
        diff = abs(n2/d - PI)
        N,D = n2,d
#print '%s %d' % (name, number)
print '%d/%d'%(int(N),int(D))
