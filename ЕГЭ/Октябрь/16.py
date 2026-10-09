'''
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f(n-1)
    if n > 1 and n % 2 == 1:
        return 2*f(n-2)
print(f(26))
'''
'''
def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return 3*f(n-1)-f(n-2)
print(f(6))
'''
'''
def f(n):
    if n > 18:
        return n
    if n <= 18:
        return 3*f(n+1)+n+8
print(f(9))
'''
'''
def f(n):
    if n < 5:
        return 5 - n
    if n >= 5 and n % 3 == 0:
        return 4*(n-1)*f(n-5)
    if n >= 5 and n % 3 != 0:
        return 3*n + 2*f(n-1) + f(n-2)
print(f(20))
'''
'''
f = [0]*1000
for n in range(len(f)):
    if n <= 3:
        f[n] = n
    if 3 < n <= 32:
        f[n] = n//4 + f[n-3] 
    if n > 32:
        f[n] = 2*f[n-5]
print(f[100])
'''
'''
def f(n):
    if n < 0:
        return -n
    if n % 2 == 0:
        return 2*n + 1 + f(n-3)
    if n % 2 != 0:
        return 4*n + 2*f(n-4)
print(f(33))
'''
'''
def f(n):
    if n <= 70:
        return f(n+2) + 2*f(3*n)
    if n > 70:
        return n - 50
print(f(40))
'''
'''
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) - 2*g(n-1)
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) + 2*g(n-1)
print(g(21))
'''
'''
#f = [0]*1000
#for n in range(-50, len(f)/2):
#    if n <= 0:
#        f[n] = n
#    if n > 0 and n % 2 == 0:
#        f[n] = f[n//2] + 5*n
#    if n > 0 and n % 2 != 0:
#        f[n] = f[n-4] - f[n-6]
#print(f[70] + f[56] - f[66] - f[44])

def f(n):
    if n <= 0:
        return n
    else:
        if n % 2 == 0:
            return f(n//2) + 5*n
        else:
            return f(n-4) - f(n-6)
print(f(70) + f(56) - f(66) - f(44))
''' 
'''
f = [0]*10000
for n in range(len(f)):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n*f[n-1]
print((f[2023] - f[2022])/f[2020])
'''
'''
f = [0]*10000
for n in range(len(f)):
    if n < 7:
        f[n] = 7
    else:
        if n % 3 != 0:
            f[n] = 5 - f[n-1]
        else:
            f[n] = 3 + f[n-1]
print(f[3015])
'''
'''
f = [0]*10000
for n in range(len(f)):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = f[n-1] + n*f[n-1]
print(f[5997]/f[5995])
'''
'''
f = [0]*1000
for n in range(len(f)):
    if n < 15:
        f[n] = 4
    else:
        if n % 3 == 0:
            f[n] = f[2*int(n/3)] + n - 1
        else:
            f[n] = f[n-1] + 3
for i in range(len(f)):
    if f[i] == 251:
        print(i)
'''
'''
f = [0]*10000
for n in range(len(f)):
    if n < 3:
        f[n] = 1
    else:
        if n % 2 != 0:
            f[n] = f[n-1] + n
        else:
            f[n] = f[n-3] + 2*n
print(f[2048] - f[2041])
'''
'''
def f(n):
    if n < 50:
        return n
    if n > 49:
        return 2*g(50-n//2)

def g(n):
    if n > 40:
        return 10
    if n < 41:
        return 30 + f(n+600//n)

print(f(80))
'''
'''
f = [0]*10000
g = [0]*10000
sum = 0
for n in range(len(g)):
    if n == 1:
        f[n] = 1
        g[n] = 1
    if n > 1:
        f[n] = f[n-1] - 2*g[n-1]
        g[n] = f[n-1] + g[n-1] + n
for i in range(len(str(g[36]))):
    sum += int(str(g[36])[i])
print(sum)
'''
'''
f = [0]*10000
for n in range(len(f)):
    if n < 4:
        f[n] = 1
    if n > 3:
        f[n] = f[n-1] * (n-3)
print(f[1401]/f[1397])
'''
'''
f = [0]*10000
for n in range(len(f)):
    if n <= 3:
        f[n] = 1
    if n > 3:
        f[n] = (n+3)*f[n-2]
print(f[2028]/f[2024])
'''
'''
f = [0]*10000
g = [0]*10000
for n in range(len(f)):
    if n == 3:
        f[n] = 1
        g[n] = 1
    if n > 3:
        f[n] = 5*f[n-1] + 6*g[n-1] - 3*n + 8
        g[n] = 6*f[n-1] + 5*g[n-1] + 3
print(f[9] + g[9])
'''   
'''
sum = 0
f = [0]*1000
for n in range(len(f)):
    if n == 0:
        f[n] = 1
    if n > 0:
        f[n] = 2*f[1-n] + 3*f[n-1] + 2
    if n < 0:
        f[n] = -f[-n]
for i in range(len(str(f[50]))):
    sum += int(str(f[50])[i])
print(sum)

from functools import cache
@cache
def f(n):
    if n == 0:
        return 1
    if n > 0:
        return 2*f(1-n) + 3*f(n-1) + 2
    if n < 0:
        return -f(-n)

sum = 0
for i in range(len(str(f(50)))):
    sum += int(str(f(50))[i])
print(sum)
'''
'''
f = [0]*100000
for n in range(len(f)):
    if n >= 7777:
        f[n] = n
    if n < 7777:
        f[n] = n + 5 + f[n+5]
print(f[1101] - f[1111])
'''
'''
def f(n):
    if n >= 7777:
        return n
    if n < 7777:
        return n + 5 + f(n+5)
print(f(1101) - f(1111))
'''
'''
f = [0]*100000
for n in range(len(f)):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = 2*n + f[n-1]

sum = 0
for i in range(len(str(f[57693]))):
    sum += int(str(f[57693])[i])
print(sum**2)
'''
'''
f = [0]*10000
for n in range(len(f)):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = (2*n-1)*f[n-1]
print(f[3516]/f[3513])
'''
'''
from functools import cache
@cache
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (2*n-1)*f(n-1)

for n in range(1, 3517):
    f(n)

print(f(3516)/f(3513))
'''