n = int(input())
while True:
    condition = True
    for i in str(n):
        if i != "4" and i != "7":
            condition = False
    if condition == True :
        break
    else:
        n = n - 1
print(n)