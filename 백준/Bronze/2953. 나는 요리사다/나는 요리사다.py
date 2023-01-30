total_score = []
for _ in range(5) :
    score_list = map(int,input().split())
    total = sum(score_list)
    total_score.append(total)
max_score = max(total_score)
max_num = total_score.index(max_score) + 1
print(max_num, max_score)