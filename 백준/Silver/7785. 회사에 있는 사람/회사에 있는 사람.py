n = int(input())
in_out = {}
answer = []
for _ in range(n) :
    a,b = input().split()
    in_out[a] = b
for key, value in in_out.items() :
    if value == 'enter' : answer.append(key)
answer.sort(reverse = True)
print(*answer, sep = '\n')