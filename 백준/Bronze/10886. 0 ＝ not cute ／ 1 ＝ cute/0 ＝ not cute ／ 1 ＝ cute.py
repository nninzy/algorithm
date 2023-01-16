N = int(input())
cnt_1, cnt_0 = 0, 0
for _ in range(N) :
    if input() == '1' : cnt_1 += 1
    else : cnt_0 += 1
print('Junhee is cute!' if cnt_1 > cnt_0 else 'Junhee is not cute!')