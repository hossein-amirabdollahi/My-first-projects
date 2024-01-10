n = int(input())
e2f = dict()
kh = []
for i in range (0, n) :
    vo = input()
    vo = vo.strip()
    lvo = vo.split()
    e2f[lvo[0]] = lvo[1]
f = input()
f = f.strip()
lf = f.split()
for i in lf :
    if i in e2f :
        kh.append(e2f[i])
    else :
        kh.append(i)
print(' '.join(kh))