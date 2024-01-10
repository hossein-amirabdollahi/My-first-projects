import random
x = 1
y = 100

while True:
    answer = input('''Please think of a number between 1 and 99 in your mind 
and enter "ready" when you are ready: ''')
    if answer == 'ready':
        break
faunded = 0

while True :

    hads = random.randint(x, y)
    print(hads)
    user_answer = input('''thats it?... 
If said right please enter "right"
but if not, guid me with "less" or "more": ''')
    if user_answer == 'right' :
        break
    while True:
        if user_answer == 'right' :
            faunded+=1
            break
        elif user_answer == 'more' :
            x = hads + 1
            break
        elif user_answer == 'less' :
            y = hads - 1
            break
        else :
            print('''Please if my guess is wrong, guide me just with "less" or "more" : ''')
            user_answer = input('"less" or "more": ')
    if faunded != 0 :
        break
print("yesssss I can do it ... just with your guidance!!")