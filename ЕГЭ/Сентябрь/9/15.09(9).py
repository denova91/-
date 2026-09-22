'''
#8497
cnt = 0
f = open('9_8497.csv')
for s in f:
    a = list(map(int,s.split(';')))
    a.sort()
    if len(a) == len(set(a)):
        if 3*(a[0] + a[-1]) >= 2*(a[1] + a[2] + a[3]):
            cnt += 1
print(cnt)
'''
'''
#5728
cnt = 0
f = open('9-koord_5728.csv')
for s in f:
    a = list(map(int,s.split(';')))
    if a[0] * a[1] * a[2] * a[3] > 0:
        cnt += 1
print(cnt)
'''
'''
#5664
cnt = 0
f = open('9_5664.csv')
for s in f:
    a = list(map(int,s.split(';')))
    if (a[0]*a[1]) % 10 == 4:
        cnt += 1
    elif (a[1]*a[2]) % 10 == 4:
        cnt += 1
    elif (a[0]*a[2]) % 10 == 4:
        cnt+= 1
print(cnt)
'''
'''
#5489
cnt = 0
f = open('
'''
'''
#4321
cnt = 0
f = open('9_4321.csv')
for s in f:
    a = sorted(list(map(int, s.split(';'))))
    
    if (a[0]**3 + a[1]**3) > ((a[2]+a[3]+a[4])**2):
        cnt += 1
print(cnt)
'''
'''
#3362
cnt = 0
f = open('9_3362.csv')
for s in f:
    a = list(map(int, s.split(';')))
    m1 = [x for x in a if x%2==0]
    m2 = [x for x in a if x%2!=0]
    if sum(m2) > sum(m1):
        cnt += 1
print(cnt)
'''
'''
#13824(не получ)
def f(c):
    res = 1
    for i in range(c):
        res *= i
    return res
    
cnt = 0
c = 0
f = open('9_3362.csv')
for s in f:
    a = list(map(int, s.split(';')))
    c += 1
    if all(a[i]%2 == a[i+1]%2 for i in range(len(a)-1)):
        x, y = [], []
        for j in a:
            if a.count(j) > 1:
                x += [j]
            else:
                y += [j]
        a = list(set(a))
        if (sum(y))*3 >= int(f(x)):
            cnt += c
print(cnt)
'''
'''
#12726
cnt = 0
f = open('9_12726.csv')
for s in f:
    a = list(map(int, s.split(';')))
    m1 = [x for x in a if a.count(x)==3]
    m2 = [x for x in a if a.count(x)==1]
    c1 = [x for x in a if x%2==0]
    c2 = [x for x in a if x%2!=0]
    if len(c1) > len(c2):
        if len(m1) == 3 and len(m2) == 4:
            cnt += 1
print(cnt)
'''
'''
#24347(решил в классе)
'''
'''
#24359
res = []
f = open('9_24359.csv')
for s in f:
    a = list(map(int, s.split(';')))
    r3 = [x for x in a if a.count(x) == 3]
    r2 = [x for x in a if a.count(x) == 2]
    r1 = [x for x in a if a.count(x) == 1]
    
    if len(r3) == 3 and len(r2) == 2 and len(r1) == 3:
        if (sum(r3) + sum(r2)) > sum(r1):
            res.append(sum(a))
print(res[-1])
'''         

#24360
f = open('9_24360.csv')
for s in f:
    a = list(map(int, s.split(';')))
    r2 = [x for x in a if a.count(x) % 2 == 0]
    qm = min(a)**2
    f1 = (a.count(qm) == 1)
    
    if len(r2) == 6:
        print(r2, a)














































    





































