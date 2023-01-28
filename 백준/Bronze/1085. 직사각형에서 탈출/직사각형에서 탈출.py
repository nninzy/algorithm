answers = list(map(int, input().split()))
for i in range(2) :
    answers[2 + i] -= answers[i]
print(min(answers))