matrix = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(4) :
    a,b,c,d = map(int, input().split())
    for i in range(a,c) :
        for j in range(b,d) :
            matrix[i][j] = 1

result = 0
for row in matrix:
    result += sum(row)
print(result)