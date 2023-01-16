N = int(input())
file = []
for _ in range(N) :
    file.append(input())
answer = []
for item in file[0] :
    answer.append(item)
for item in file :
    for i in range(len(answer)) :
        if item[i] != answer[i] :
            answer[i] = '?'
print(*answer, sep = '')