k, n = map(int, input().split())
k_list = []

for i in range(k):
    k_list.append(int(input()))

start = 1
end = max(k_list)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(k):
        cnt += k_list[i] // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)