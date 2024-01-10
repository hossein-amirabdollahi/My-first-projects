L = []
pr = []
# "pr" is contracted form of "price"

pe = []
# "pe" is contracted form of "performance"

c = 0
n = int(input())

for i in range (0, n) :
    Li = input()
    Li = Li.split(' ')
    for f in range(0, len(Li)) :
        Li[f] = int(Li[f])
    L = L + Li

for i in range (0, (n * 2)) :
    if i == 0 or i%2 == 0 :
        pr.append(L[i])
    else :
        pe.append(L[i])

for k in range(0, n) :
    for i in range(0, n) :
        if pr[k] < pr[i] and pe[k] > pe[i] :
            c = c + 1

if c == 0 :
    print('poor irsa')
else :
    print('happy irsa')