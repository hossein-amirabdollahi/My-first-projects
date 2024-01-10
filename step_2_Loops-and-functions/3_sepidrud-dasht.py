j = 0
b = 0
c = 1
while True :
    x = int(input())
    if x == 3 :
        c = c + 1
        j = j + x
        b = b + 1
    elif x == 1 :
        c = c + 1
        j = j + x
    elif x == 0 :
        c = c + 1
    else :
        print("bishtar deghat kon !!!!")
    if c == 31 :
        break
print(j, b)
