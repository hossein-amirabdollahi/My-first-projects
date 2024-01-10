L = []
while True :
    x = int(input())
    if x == -1 :
        break
    L.append(x)
L.sort(reverse=True)
print(L[0], L[1])