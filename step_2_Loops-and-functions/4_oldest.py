b = 10
while True :
    sen = int(input())
    if (sen > b) and (sen >= 10) and (sen < 90) :
        b = sen
    elif sen == -1 :
        break
    else :
        False
print(b)
