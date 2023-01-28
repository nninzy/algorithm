N = int(input())
ran = N if N < 100 else 54
answer = 0
for i in range(N - ran, N) :
    i_sum = 0
    for j in range(len(str(i))) :
        i_sum += int(str(i)[j])
    if (i + i_sum) == N : answer = i; break;
print(answer)