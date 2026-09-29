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
        
