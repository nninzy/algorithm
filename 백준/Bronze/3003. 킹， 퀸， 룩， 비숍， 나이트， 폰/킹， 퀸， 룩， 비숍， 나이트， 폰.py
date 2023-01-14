changed = list(map(int,input().split()))
std = [1, 1, 2, 2, 2, 8]
answer = []
for i in range(len(changed)) :
    answer.append(std[i] - changed[i])
print(*answer)