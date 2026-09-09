'''
#1
a = input()
cnt = 0
for i in range(len(a)):
    if a[i] == '(':
        cnt += 1
    elif a[i] == ')':
        cnt -= 1
        if cnt < 0:
            print('Error')
            break
if cnt != 0:
    print('Error')
'''
'''
#2
print(eval(input()))
'''
'''
#3
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def sokr(a):
    u = a.find('/')
    x1 = int(a[:u])
    x2 = int(a[(u+1):])
    limit = min(x1, x2)

    for i in range(2, limit + 1):
        if is_prime(i):
            if x1 % i == 0 and x2 % i == 0:
                x1 //= i
                x2 //= i
                y = str(x1) + '/' + str(x2)
                return y, x1, x2
    return a, x1, x2


a = input()

u = a.find('/')
x1 = int(a[:u])
x2 = int(a[(u+1):])
n = []
while True:
    if math.gcd(x1, x2) == 1:
        n.append(a)
        break
    n.append(a)
    a, x1, x2 = sokr(a)

for i in range(len(n)):
    if n[-1] != n[i]:
        print(n[i], '=', end=' ')
    else:
        print(n[i])

###########
#(рефакторинг от дипсика)
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def sokr(a):
    num_str, den_str = a.split('/')
    x1 = int(num_str)
    x2 = int(den_str)

    limit = min(x1, x2)

    for i in range(2, limit + 1):
        if is_prime(i):
            if x1 % i == 0 and x2 % i == 0:
                x1 //= i
                x2 //= i
                y = f"{x1}/{x2}"
                return y, x1, x2
                
    return a, x1, x2

a = input()
steps = []
x1, x2 = map(int, a.split('/'))

while True:
    steps.append(a)
    if math.gcd(x1, x2) == 1:
        break
    a, x1, x2 = sokr(a)

print(" = ".join(steps))
'''
'''
#4
n = int(input("Введите количество строк: "))
matrix = []
res = []

for i in range(n):
    row = list(map(int, input(f"Введите строку ({i + 1}) через пробел: ").split()))
    matrix.append(row)

print(matrix, len(matrix), len(matrix[0]))

res = [0] * len(matrix[0])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        res[j] += matrix[i][j]
        
print(res)
'''
'''
#6
a = input()
g = []
s = ""
for w in a.split():
    if len(s) + len(w) + (1 if s else 0) <= 70:
        s = (s + " " if s else "") + w
    else:
        if s:
            g.append(s)
        s = w
if s:
    g.append(s)
print(g)
'''





























