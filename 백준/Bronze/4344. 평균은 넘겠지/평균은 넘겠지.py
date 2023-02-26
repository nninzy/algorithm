C = int(input())
for _ in range(C) :
    students = list(map(int, input().split()))
    N = students[0]; score_list = students[1:]
    aver = sum(score_list) / N
    num_high = 0
    for item in score_list :
        if item > aver :
            num_high += 1
    perct = round((num_high / N) * 100, 3)
    num1, num2 = str(perct).split('.')
    while len(num2) < 3:
        num2 += '0'
    print(num1 + '.' + num2 + '%')