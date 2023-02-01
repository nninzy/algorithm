T = int(input())
for _ in range(T):
    scores1 = list(map(int, input().split()))
    scores2 = sorted(scores1)[1:4]
    answer = 'KIN' if (scores2[2] - scores2[0]) >= 4 else sum(scores2)
    print(answer)