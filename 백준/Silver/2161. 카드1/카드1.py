n = int(input())
num_list = list(range(1, n+1)); out_list = []
while len(num_list) != 1 :
    out_list.append(num_list.pop(0))
    num_list.append(num_list.pop(0))
print(*out_list, *num_list)