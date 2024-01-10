fajr = ''
kh = ''
c = 0
while True :
    vorudi = input()
    fajr = fajr + vorudi + ',' 
    c = c + 1
    if c == 10 :
        break
for i in range(0, len(fajr)) :
    if fajr[i] == ',':
        kh = kh[:1].upper() + kh[1:].lower()
        print(kh)
        kh = ''
    else :
        kh = kh + fajr[i]
