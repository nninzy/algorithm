n, m = map(int, input().split())
a = []; b = []
for i in range(1, n + 1) :
    a.append(list(map(int, input().split())))
for j in range(1, n + 1) :
    b.append(list(map(int,input().split())))
for k in range(n) :
    for l in range(m) :
        a[k][l] += b[k][l]
for x in range(n) :
    print(*a[x])