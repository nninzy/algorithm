def d(n) :
    sum = n
    for a in str(n) :
        sum += int(a)
    return sum

def gener(num) :
    cnt = 0
    if num <= 100 : ctrl = 0
    elif num <= 1000 : ctrl = num - 30
    else : ctrl = num - 50
    for i in range(ctrl, num) :
        if d(i) == num :
            cnt += 1
    return cnt

for number in range(1, 10000) :
    if gener(number) == 0 :
        print(number)