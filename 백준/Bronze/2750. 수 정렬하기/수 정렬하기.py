n = int(input())
num_list = []
for _ in range(n) :
    num_list.append(int(input()))
num_list.sort()
print(*num_list, sep = '\n')