T = int(input())
for t in range(T) :
    score = input()
    total = 0; cnt = 1
    for i in range(len(score)) :
        if score[i] == 'O' :
            total += cnt
            cnt += 1
        else :
            cnt = 1
    print(total)