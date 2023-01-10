T = int(input())
for t in range(1, T+1) :
    num_list = list(map(int, input().split()))
    # 소수점일 경우 반올림 필요
    aver = round(sum(num_list) / 10)
    test_case = '#' + str(t)
    print(test_case, aver)