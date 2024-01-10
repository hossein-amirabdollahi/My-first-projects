v = input()
v = v.lower()
c = 0
miane = int(len(v) / 2)
tedad = len(v) - 1
for i in range(0, len(v)) :
    l = tedad - i
    if v[i] == v[l] :
        c = c + 1
    else :
        print('not palindrome')
        break
if c == len(v) :
    print('palindrome')
    