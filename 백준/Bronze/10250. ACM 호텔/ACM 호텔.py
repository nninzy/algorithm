T = int(input())
for _ in range(T) :
    h, w, n = map(int, input().split())
    my = [n // h, h] if n % h == 0 else [n // h + 1, n % h]
    print(my[1] * 100 + my[0])