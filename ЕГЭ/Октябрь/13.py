
# 1 -> 20  +1 *2
a = [0]*100
a[1] = 1

for i in range(1, 21):
    a[i+1] += a[i]
    a[i*2] += a[i]

    