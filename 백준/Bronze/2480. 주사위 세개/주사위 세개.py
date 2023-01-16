n_list = list(map(int, input().split()))
if n_list.count(n_list[0]) == 3 :
    print(10000 + n_list[0] * 1000)
elif n_list.count(n_list[0]) == 2 :
    print(1000 + n_list[0] * 100)
elif n_list.count(n_list[1]) == 2 :
    print(1000 + n_list[1] * 100)
else :
    print(100 * max(n_list))