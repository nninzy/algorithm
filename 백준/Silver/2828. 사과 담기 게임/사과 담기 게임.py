n,m = map(int, input().split())
j = int(input())

basket_l = 1
basket_r = m
result = 0
for _ in range(j):
    drop = int(input())
    if basket_l <= drop <= basket_r:
        result += 0
    elif drop < basket_l:
        cnt = basket_l - drop
        basket_l -= cnt
        basket_r -= cnt
        result += cnt
    else:
        cnt = drop - basket_r
        basket_r += cnt
        basket_l += cnt
        result += cnt
print(result)