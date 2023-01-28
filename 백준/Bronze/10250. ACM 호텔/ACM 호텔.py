T = int(input())
for _ in range(T) :
    h, w, n = map(int, input().split())
    if n % h == 0 :
        my_w, my_h = n // h, h
    else :
        my_w, my_h = (n // h + 1), n % h
    if w < 100 :
        answer = my_h * 100 + my_w
    else :
        answer = my_h * (10**(len(str(w)) - 1)) + my_w
    print(answer)
