T = int(input())
coin = [25, 10, 5, 1]
for _ in range(T) :
    c = int(input())
    left = c
    coin_cnt = []
    for i in coin :
        coin_cnt.append(left // i)
        left = left % i
    print(*coin_cnt)