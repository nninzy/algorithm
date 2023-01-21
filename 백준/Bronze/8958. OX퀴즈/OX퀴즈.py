T = int(input())
for t in range(T) :
    score = input()
    total = 0; cnt = 1
    for item in score :
        if item == 'O' :
            total += cnt
            cnt += 1
        else :
            cnt = 1
    print(total)