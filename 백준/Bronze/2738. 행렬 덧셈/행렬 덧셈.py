n, m = map(int, input().split())
a = []
for i in range(n) :
    a.append(list(map(int, input().split())))
for j in range(n) :
    b_list = list(map(int, input().split()))
    for k in range(m) :
        a[j][k] += b_list[k]
for x in range(n) :
    print(*a[x])