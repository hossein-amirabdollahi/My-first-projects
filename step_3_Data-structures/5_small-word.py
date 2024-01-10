v = input()
ca = 0
sm = 0
capital = v.upper()
small = v.lower()
for i in range(0, len(v)) :
    if v[i] == capital[i] :
        ca = ca + 1
    else :
        sm = sm + 1
if sm < ca :
    print(capital)
else :
    print(small)