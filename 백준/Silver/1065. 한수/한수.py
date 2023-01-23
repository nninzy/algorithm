def arithmetic(num) :
    a = str(num)[0]; b = str(num)[1]; c = str(num)[2]
    result = False
    if int(a) + int(c) == 2 * int(b) : result = True
    return result

N = int(input())
cnt = 0
for i in range(1, N + 1) :
    if i < 100 :
        cnt += 1
    else :
        if arithmetic(i) :
            cnt += 1
print(cnt)