'''
def f(n, p):
    a = ''
    while n > 0:
        a += str(n % p)
        n //= p
    return a[::-1]

for x in '0123456789ABCDEF':
    a1 = '1F3B' + x + '75'
    a2 = '5D' + x + '3B'
    a = int(a1, 16) + int(a2, 16)
    if a % 11 == 0:
        print(a//11)
'''
'''
def f(n, p):
    a = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ'
    while n > 0:
        a += str(n % p)
        n //= p
    return a[::-1]

a = 2*2401**525 + 3*343**524 - 4*39**523 + 5*49**522 - 6*7**521 - 35

print(a//49**1000)
'''
'''
alf = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
m = 0
for x in alf[:25]:
    a = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if a % 24 == 0:
        print(x, a//24)
'''
'''
for p in range(7, 36):
    a1 = int('2465123', p) 
    a2 = int('251341', p)
    s = a1 + a2
    if s % 17 == 0:
        print(s//17)
        break
'''
'''
for p in range(8, 36):
    a1 = int('11353712', p) 
    a2 = int('135421', p)
    s = a1 + a2
    if s % 31 == 0:
        print(s//31)
        break
'''
'''
for p in range(18, 36):
    a1 = int('22A12E', p) 
    a2 = int('2F1391', p)
    a3 = int('1H05D0', p)
    s = a1 + a2 - a3
    if s % 19 == 0:
        print(s//19)
        break
'''

for p in range(11, 36):
    for x in range(1000):
        a1 = int('29A1', p) 
        a2 = int('47771', p)
        a3 = int('12A', p)
        if (a1 + a2 + a3) == (1_000_000 + x):
            print(p)