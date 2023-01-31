n_value = [int(input()) for _ in range(10)]
n_cnt = [n_value.count(n) for n in n_value]
print(sum(n_value)//10, n_value[n_cnt.index(max(n_cnt))], sep = '\n')