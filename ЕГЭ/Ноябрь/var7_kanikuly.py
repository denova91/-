# 1
# ответ: 29

# 2
print('x y w z')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                f = (not (x <= y)) or ((not z) == (w <= x)) or w
                if f == 0:
                    print(x, y, w, z, f)
# ответ: wzxy

# 3
# ответ: 130

# 4
# ответ: 011

# 5
for N in range(1, 1000):
    bN = bin(N)[2:]
    if N % 4 == 0:
        bN = bN + bN
    else:
        bN = bN + bN[::-1]
    res = int(bN, 2)
    if res >= 544:
        print(N, res)
        break
# ответ: 17

# 6
from turtle import *
tracer(0)
k = 30
lt(90)
for i in range(3):
    fd(2*k)
    rt(90)
    fd(3*k)
    lt(90)
rt(180)
fd(6*k)
rt(90)
fd(9*k)
pu()
bk(4*k)
rt(90)
pd()
for i in range(3):
    fd(1*k)
    rt(90)
    fd(2*k)
    lt(90)
rt(180)
fd(4*k)
rt(90)
fd(6*k)
rt(90)
fd(1*k)
pu()
for x in range(-2, 12):
    for y in range(-3, 8):
        goto(x*k, y*k)
        dot(3)
done()
# ответ: 16

# 7
# ответ: 17

# 8
# ответ: 392

# 9
# условие не нашел

# 11
# ответ: 138

# 12
# ответ: 129

# 13
# ответ: 934

# 14
s = 6**2025 + 6**25
for x in range(1000, 0, -1):
    v = s - x
    r = ''
    while v > 0:
        r += str(v % 6)
        v //= 6
    if r.count('0') == 2002:
        print(x)
        break
# ответ: 972

# 15
def delitel(n, m):
    return n % m == 0

ans = 0
for A in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        B = 200 <= x <= 300
        if not (delitel(x, A) or ((not B) or (not delitel(x, 77)))):
            ok = False
            break
    if ok:
        ans = A
print(ans)
# ответ: 231

# 16
f = [0]*10000
for n in range(len(f)):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n + f[n-1]
print(f[3000] - f[2000])
# ответ: 2500500

# 17
f = open('17var07.txt')
a = list(map(int, f))
m = min(a)
cnt = 0
res = []
for i in range(len(a) - 1):
    if a[i] % 44 + a[i+1] % 44 == m:
        cnt += 1
        res.append(abs(a[i] - a[i+1]))
print(cnt, min(res))
# ответ: 178 593

# 18
# ответ: 2661 1088
