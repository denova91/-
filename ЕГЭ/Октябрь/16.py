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
'''
f = [0]*100000
g = [0]*100000

for n in range(len(g)-1, -1, -1):
    if n >= 22560:
        g[n] = n/23 + 33
    if n < 22560:
        g[n] = g[n+11] - 4

for n in range(len(f)):
    if n >= 21:
        f[n] = f[n-8] + 1095
    if n < 21:
        f[n] = 10*(g[n-7]-36)

print(f[548])
'''
'''
f = [0]*100000
g = [0]*100000

for n in range(len(f)):
    f[n] = 3*(g[n-2] + 5)
    if n < 8:
        g[n] = 3*n
    else:
        g[n] = g[n-3] + 2
print(f[12345])
'''
'''
f = [0]*10000

for n in range(len(f)):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n*f[n-1]
print((f[3038] + 5*f[3037])/f[3036])
'''
'''
f = [0]*100000
g = [0]*100000

for n in range(len(f)):
    f[n] = 3*g[n-3] + 7
    if n <= 20:
        g[n] = n + 2
    else:
        g[n] = g[n-3] + 1
print(f[37811])
'''
'''
from functools import lru_cache
@lru_cache

def f(n):
    if n < 10:
        return 3
    else:
        return (n + 4)*f(n-5)

for n in range(1, 257488):
    f(n)

print((f(257487)//683 + 67*f(257477))//f(257472))
'''
'''
f = [0]*10_000

for n in range(len(f)):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n*f[n-1]
print((f[2024] - 2*f[2023])/f[2022])
'''
'''
f = [0]*300_000
g = [0]*300_000

for n in range(len(g)-1, -1, -1):
    if n >= 248045:
        g[n] = n/20 + 28
    if n < 248045:
        g[n] = g[n+9] - 4

for n in range(len(f)):
    if n < 19:
        f[n] = 6*(g[n-7] - 36)
    if n >= 19:
        f[n] = f[n-4] + 3580
print(f[673])
'''
'''
f = [0]*10_000
g = [0]*10_000

for n in range(len(f)):
    if n < 100:
        g[n] = n
    if n >= 100:
        g[n] = f[n-3] + 1
    f[n] =  g[n-2]
print(f[5000])
'''
'''
f = [0]*100_000
g = [0]*100_000

for n in range(len(f)):
    f[n] = 2*(g[n-3] + 8)
    if n < 10:
        g[n] = 2*n
    else:
        g[n] =  g[n-2] + 1
print(f[15548])
'''
'''
f = [0]*100_000
g = [0]*100_000

for n in range(len(f)):
    f[n] = g[n-1]
    if n <= 9:
        g[n] = 3*n
    else:
        g[n] =  g[n-2] + 1
print(f[47995])
'''
'''
import sys 

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(5000)

def f(n):
    if n >= 21:
        return f(n-8) + 1095
    else:
        return 10*(g(n-7) - 36)

def g(n):
    if n >= 22560:
        return n/23 + 33
    else:
        return g(n+11) - 4

print(f(548))

sys.setrecursionlimit(get_limit)
'''
'''
import sys

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(5000)

def f(n):
    return 3*(g(n-2) + 5)

def g(n):
    if n < 8:
        return 3*n
    else:
        return g(n-3) + 2

print(f(12345))

sys.setrecursionlimit(get_limit)
'''
'''
import sys

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(5000)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n*f(n-1)

print((f(3038) + 5*f(3037))/f(3036))

sys.setrecursionlimit(get_limit)
'''
'''
import sys

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(15000)

def f(n):
    return 3*g(n-3) + 7

def g(n):
    if n <= 21:
        return n + 2
    else:
        return g(n-3) + 1

print(f(37811))

sys.setrecursionlimit(get_limit)
'''
'''
import sys
from functools import lru_cache

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(25000)
@lru_cache(None)

def f(n):
    if n < 10:
        return 3
    else:
        return (n + 4)*f(n-5)

for n in range(260000):
    f(n)

print((f(257487)/683 + 67*f(257477))/f(257472))

sys.setrecursionlimit(get_limit)
'''
'''
import sys

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(10000)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n*f(n-1)

print((f(2024) - 2*f(2023))/f(2022))

sys.setrecursionlimit(get_limit)
'''
'''
import sys

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(30000)

def f(n):
    if n >= 19:
        return f(n-4) + 3580
    if n < 19:
        return 6*(g(n-7) - 36)

def g(n):
    if n >= 248045:
        return n/20 + 28
    else:
        return g(n+9) - 4

print(f(673))

sys.setrecursionlimit(get_limit)
'''
'''
import sys

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(10000)

def f(n):
    return g(n-2)

def g(n):
    if n < 100:
        return n
    else:
        return f(n-3) + 1

print(f(5000))

sys.setrecursionlimit(get_limit)
'''
'''
import sys

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(10000)

def f(n):
    return 2*(g(n-3) + 8)

def g(n):
    if n < 10:
        return 2*n
    else:
        return g(n-2) + 1

print(f(15548))

sys.setrecursionlimit(get_limit)
'''
'''
import sys

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(50000)

def f(n):
    return g(n-1)

def g(n):
    if n <= 9:
        return 3*n
    else:
        return g(n-2) + 1

print(f(47995))

sys.setrecursionlimit(get_limit)
'''
'''
import sys

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(20000)

def f(n):
    if n < 31054:
        return f(n+4) + 3020
    else:
        return 3*(g(n-2) - 15)

def g(n):
    if n < 28:
        return 3*n - 4  
    else:
        return g(n-5) - 15

print(f(15))

sys.setrecursionlimit(get_limit)
'''
'''
import sys
from functools import lru_cache

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(10000)

@lru_cache(None)
def f(n):
    if n < 128:
        return 5*g(n-7) + 29
    else:
        return f(n-5) + 1092

@lru_cache(None)
def g(n):
    if n > 303728:
        return n - 15
    else:
        return g(n+8)/2 - 109

for n in reversed(range(300000)):
    g(n)

for n in range(5000):
    f(n)

print(f(2049))

sys.setrecursionlimit(get_limit)
'''
'''
import sys
from functools import lru_cache

get_limit = sys.getrecursionlimit()
sys.setrecursionlimit(3000) 

@lru_cache(None)
def f(n, x):
    if n >= 3000:
        return n
    else:
        return n + x + f(n+2, x)

for x in range(-1000, 1000):
    if f(2984, x) - f(2988, x) == 5916:
        print(x)

sys.setrecursionlimit(get_limit)
'''
