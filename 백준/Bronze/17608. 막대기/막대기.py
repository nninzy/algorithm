import sys
N = int(sys.stdin.readline())
sticks = [int(sys.stdin.readline()) for i in range(N)][::-1]
std = sticks[0]
cnt = 1
for h in sticks:
    if std - h < 0:
        cnt += 1
        std = h
print(cnt)