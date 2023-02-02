upside = []
N = int(input())
h = list(map(int, input().split()))
cnt = 0
for i in range(1, N):
    a = h[i] - h[i-1]
    if a > 0 : cnt += a
    else :
        if cnt != 0: upside.append(cnt)
        cnt = 0
if cnt != 0 : upside.append(cnt)
print(sorted(upside)[-1] if len(upside) > 0 else 0)