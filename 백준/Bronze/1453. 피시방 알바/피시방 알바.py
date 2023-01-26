space_list = [0] * 100
n = int(input())
hope_list = list(map(int, input().split()))
over_cnt = 0
for i in range(n) :
    if space_list[hope_list[i] - 1] == 0 : space_list[hope_list[i] - 1] = 1
    else : over_cnt += 1
print(over_cnt)