import sys
T = int(sys.stdin.readline())
for _ in range(T) :
    N = int(sys.stdin.readline())
    n_list = map(int, sys.stdin.readline().split())
    print(sum(n_list))