dif_list = []; sam_list = []
for _ in range(3) :
    angle = int(input())
    if angle in dif_list : sam_list.append(angle)
    else : dif_list.append(angle)
if (sum(dif_list) + sum(sam_list)) != 180 : print('Error')
elif len(dif_list) == 3 : print('Scalene')
elif len(dif_list) == 2 : print('Isosceles')
else : print('Equilateral')