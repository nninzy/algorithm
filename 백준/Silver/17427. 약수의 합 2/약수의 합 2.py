A = int(input())
answer = 0
for num in range(1,A+1) :
    answer+= num * (A//num)
print(answer)