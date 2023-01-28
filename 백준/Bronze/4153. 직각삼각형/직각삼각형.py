while True :
    len_list = list(map(int, input().split()))
    if len_list == [0, 0, 0] : break
    max_len = max(len_list)
    cal = max_len ** 2
    for len in len_list :
        if len != max_len : cal -= (len ** 2)
    print('right' if cal == 0 else 'wrong')