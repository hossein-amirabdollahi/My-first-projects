def maqsum(a):
    m = 1
    for i in range(1, a) :
        if a % i == 0 :
            m = m + 1
    return m

L = []

ma = 1

caunt = 1

while caunt <= 20 :
    x = int(input())
    L.append(x)
    if maqsum(x) > ma :
        ma = maqsum(x)
    caunt += 1

bl = []

for item in L :
    if maqsum(item) == ma :
        bl.append(item)
bl.sort(reverse=True)

print(bl[0], ma)
