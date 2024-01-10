vorudi = input()
l = vorudi.split()
list_point = []
for i in l:
    list_point.append(float(i))

list_point.sort()

meeting_point = (list_point[0]+list_point[2]) / 2

def ghadr_motlagh (x):
    if x < 0 :
        x = x * (-1)
    return x
# Unfortunately I was not familiar with abs() function yet

result = ghadr_motlagh(list_point[0]-meeting_point) + ghadr_motlagh(list_point[2]-meeting_point)

if result - int(result) == 0 :
    print(int(result))
else :
    print(result)