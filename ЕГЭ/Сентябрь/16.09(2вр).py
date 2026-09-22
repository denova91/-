'''
for N in range(1, 1000):
    bN = bin(N)[2:]
    s = 0
    for i in range(len(str(bN))):
        s += int(bN[i])
    bN = bN + str(s % 2)
    for i in range(len(str(bN))):
        s += int(bN[i])
    bN = bN + str(s % 2)

    res = int(bN, 2)
    if res > 75:
        print(N, res)
'''
'''
for N in range(1, 1000):
    bN = bin(N)[2:]
    if N % 3 == 0:
        bN = bN + str(bN[-3:])
    else:
        bN = bN + str(bin((N % 3)*3)[2:])
    res = int(bN, 2)

    if res > 76:
        print(N, res)
'''
'''
cnt = 0
f = open('9 (1).csv')
for s in f:
    a = list(map(int, s.split(';')))

    r2 = [x for x in a if a.count(x) == 2]
    r1 = [x for x in a if a.count(x) == 1]

    if len(r2) == 4:
        if (sum(r2) / sum(r1)) >= 2:
            cnt += 1
print(cnt)
'''

cnt = 0
f = open('9 (1).csv')
for s in f:
    a = list(map(int, s.split(';')))
    r4 = [x for x in a if a.count(x) == 4]
    r1 = [x for x in a if a.count(x) == 1 or a.count(x) == 2]
    print(r1, r4, a)
    if len(r4) == 4:
        if (r4[0]**2) < sum(r1):
            print(r1, r4, '-----')
            cnt += 1
print(cnt)

































        
