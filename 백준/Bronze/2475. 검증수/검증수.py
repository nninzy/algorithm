num_list = list(map(int, input().split()))
total = 0
for i in range(5) :
    total += (num_list[i] ** 2)
print(total % 10)