import sys
t = int(sys.stdin.readline())
def rev(item) :
    return item[::-1]
for _ in range(t) :
    print(*list(map(rev, sys.stdin.readline().rstrip().split())))