T = int(input())
for t in range(1, T+1) :
    num_list = sorted(list(map(int, input().split())))
    test_num = '#' + str(t)
    print(test_num, num_list[-1])