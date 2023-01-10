a, b = list(map(int, input().split()))
# a/b에서 소수점은 버리기
print(a + b, a - b, a * b, int((a/b)//1), sep = '\n')