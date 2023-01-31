n_dict = {}
for _ in range(10) :
    n = int(input())
    if n in n_dict.keys() : n_dict[n] += 1
    else : n_dict[n] = 1
max_cnt = max(n_dict.values()); max_key = 0; sum = 0
for key, value in n_dict.items() :
    sum += key * value
    if value == max_cnt : max_key = key
print(sum // 10, max_key, sep = '\n')