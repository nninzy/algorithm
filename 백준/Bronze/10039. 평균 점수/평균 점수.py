students, num = [], 5
for _ in range(num) :
    score = int(input())
    score = 40 if score < 40 else score
    students.append(score)
print(int(sum(students) / num))