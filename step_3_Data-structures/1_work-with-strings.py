vo = input()
st = vo.lower()
c = 0
a = ""
for i in range (0, len(st)) :
    if st[i] == "a" or st[i] == "e" or st[i] == "i" or st[i] == "o" or st[i] == "u" :
        c = c + 1
    else :
        a = a + "." + st[i]
print(a)