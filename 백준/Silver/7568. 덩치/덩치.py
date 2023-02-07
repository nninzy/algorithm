N = int(input())
p = [[0] for _ in range(N)]
for i in range(N):
    w, h = map(int, input().split())
    p[i] += [w, h]

result = []
for a in range(N):
    rank = 1
    for b in range(N):
        if p[a][1] < p[b][1] and p[a][2] < p[b][2]:
            rank += 1
    result.append(rank)
print(*result)