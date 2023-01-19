score = {'A' : 4, 'B' : 3, 'C' : 2, 'D' : 1, 'F' : 0.0, '+' : 0.3, '0' : 0.0, '-' : -0.3}
alp = input()
answer = 0
for i in range(len(alp)) : answer += score[alp[i]]
print(answer)