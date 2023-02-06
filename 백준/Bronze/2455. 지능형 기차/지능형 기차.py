total = 0; maxi = 0
for _ in range(4):
    getOut, getOn = map(int, input().split())
    total = total + getOn - getOut
    if total > maxi:
        maxi = total
print(maxi)