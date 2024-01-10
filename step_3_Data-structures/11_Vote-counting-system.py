from collections import OrderedDict

n = int(input())

ara = []

for i in range(0, n) :
    ara.append(input())

s = OrderedDict()

for item in ara :
    s[item] = s.get(item, 0) + 1

ara2 = []

for item in list(s.keys()) :
    x = item + ' ' + str(s[item])
    ara2.append(x)

ara2.sort()

for item in ara2 :
    print(item)
