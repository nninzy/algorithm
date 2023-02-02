T = int(input())
cup = [1,2,3]
for _ in range(T):
    x, y = map(int, input().split())
    indX = cup.index(x)
    indY = cup.index(y)
    cup[indX] = y
    cup[indY] = x
print(cup[0])