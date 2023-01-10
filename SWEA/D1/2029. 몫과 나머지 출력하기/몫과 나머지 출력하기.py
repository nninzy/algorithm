T = int(input())
for t in range(1, T+1):
    a,b = list(map(int, input().split()))
    if a >= b :
        big_n, small_n = a, b
    else :
        big_n, small_n = b, a
    test_case = '#' + str(t)
    print(test_case, big_n//small_n, big_n%small_n)