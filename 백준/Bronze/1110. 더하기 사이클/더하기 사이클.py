import sys
n = sys.stdin.readline().rstrip()
cnt = 1
if len(n) == 1 : n = '0' + n
new_n = n[-1] + str(int(n[0]) + int(n[1]))[-1]
while new_n != n :
    new_n = new_n[-1] + str(int(new_n[0]) + int(new_n[1]))[-1]
    cnt += 1
print(cnt)