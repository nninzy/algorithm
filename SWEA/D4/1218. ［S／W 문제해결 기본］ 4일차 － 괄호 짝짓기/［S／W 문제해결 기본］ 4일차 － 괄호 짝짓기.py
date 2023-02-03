T = 10
for t in range(1, T+1):
    brct = [0, 0, 0, 0, 0, 0, 0, 0]
    total = ['(', ')', '[', ']', '{', '}', '<', '>']
    l = int(input())
    word = input()
    answer = 1
    for i in range(l):
        for j in [0, 2, 4, 6]:
            if word[i] == total[j]:
                brct[j] += 1
            elif word[i] == total[j+1]:
                brct[j] -= 1
                if brct[j] < 0:
                    answer = 0
                    break
    for value in brct:
        if value != 0:
            answer = 0
    print('#' + str(t), answer)