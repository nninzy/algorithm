N, K = map(int, input().split())
bus = K
for _ in range(N) :
    A, B = map(int, input().split())
    bus = bus + A - B
print('비와이')