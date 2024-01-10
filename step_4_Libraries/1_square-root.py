from math import sqrt

n = int(input())
vorudi = list()
khoruji = list()

for i in range(0, n):
    digits = float(input())
    vorudi.append(digits)

for i in vorudi:
    root = sqrt(i)
    khoruji.append(str(root))

for i in khoruji:
    if i[-1] == '0' :
        final = i + '000'
        print(final)
    else:
        dot = i.find('.')
        final1 = i[:(dot+5)]
        print(final1)