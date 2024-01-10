v = input()
c = 0
for i in range(0, len(v)) :
    if v[i] == 'h' :
        c += 1
        u = i + 1
        v = v[u:]
        break
for i in range(0, len(v)) :
    if v[i] == 'e' :
        c += 1
        u = i + 1
        v = v[u:]
        break
for i in range(0, len(v)) :
    if v[i] == 'l' :
        c += 1
        u = i + 1
        v = v[u:]
        break
for i in range(0, len(v)) :
    if v[i] == 'l' :
        c += 1
        u = i + 1
        v = v[u:]
        break
for i in range(0, len(v)) :
    if v[i] == 'o' :
        c += 1
        u = i + 1
        v = v[u:]
        break
if c == 5 :
    print('YES')
else :
    print('NO')