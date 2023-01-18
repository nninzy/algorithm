n_list = list(map(int, input().split()))
while n_list != list(range(1,6)) :
    for i in range(4) :
        if n_list[i] > n_list[i+1] :
            spare = n_list[i]
            n_list[i] = n_list[i+1]
            n_list[i+1] = spare
            print(*n_list)