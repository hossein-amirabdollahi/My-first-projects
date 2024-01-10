ma = input()
kh = ''
for i in range(0, len(ma)):
    if ma[i] == '1' :
        kh = kh + '+' + '1'
kh = kh[1:]
for i in range(0, len(ma)):
    if ma[i] == '2' :
        kh = kh + '+' + '2'
for i in range(0, len(ma)):
    if ma[i] == '3' :
        kh = kh + '+' + '3'
print(kh)
