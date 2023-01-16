N, x = map(int, input().split())
numbers = map(int, input().split())
answer_list = []
for num in numbers :
    if num < x :
        answer_list.append(num)
print(*answer_list)