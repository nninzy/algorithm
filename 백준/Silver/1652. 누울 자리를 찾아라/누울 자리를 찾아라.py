n = int(input())
matrix = []
for _ in range(n) :
    matrix.append(list(input()))
width_answer = 0; length_answer = 0
for r1 in range(n) :
    cnt1 = 0
    for c1 in range(n) :
        if matrix[r1][c1] == '.' : cnt1 += 1
        else :
            if cnt1 >= 2 :
                width_answer += 1
            cnt1 = 0
    if cnt1 >= 2 :
        width_answer += 1
for c2 in range(n) :
    cnt2 = 0
    for r2 in range(n) :
        if matrix[r2][c2] == '.' :
            if matrix[r2][c2] == '.' : cnt2 += 1
        else :
            if cnt2 >= 2 : length_answer += 1
            cnt2 = 0
    if cnt2 >= 2 :
        length_answer += 1
print(width_answer, length_answer)