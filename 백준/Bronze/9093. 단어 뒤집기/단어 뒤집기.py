t = int(input())
def rev(item) :
    return item[::-1]
for _ in range(t) :
    print(*list(map(rev, input().split())))