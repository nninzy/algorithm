m, n = map(int, input().split())
sieve = [True] * (n + 1)
sqrt_n = int((n + 1) ** 0.5)
for i in range(2, sqrt_n + 1):
    if sieve[i] == True:
        for j in range(i+i, n + 1, i):
            sieve[j] = False
n_list = [i for i in range(2, (n + 1)) if sieve[i] == True]
cnt = 0
for value in n_list :
    if value < m : cnt += 1
    else : break
print(*n_list[cnt : ], sep = '\n')