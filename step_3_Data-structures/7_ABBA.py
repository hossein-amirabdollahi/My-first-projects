vo = input()
ab = vo.find('AB')
ba = vo.find('BA')
if ba < 0 :
    print('NO')
elif ab < 0 :
    print('NO')
else:
    if ab > ba :
        avali = ba + 2
        dovomi = 'AB'
    else :
        avali = ab + 2
        dovomi = 'BA'
    vo2 = vo[avali:]
    if vo2.find(dovomi) >= 0 :
        print('YES')
    else :
        print('NO')
