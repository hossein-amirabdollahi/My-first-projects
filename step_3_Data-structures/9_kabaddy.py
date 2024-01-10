n = int(input())
L = input()
L = L.split(' ')

while True:
    if len(L) < n or len(L) > n :
        print ('pleas enter %i items'% (n))
        L = input()
        L = L.split()
    else :
        break
 
c = caunt = 0
for player in L :
    p = int(player)
    if p <= 2 :
        c = c + 1
teem = c // 3
print(teem)
