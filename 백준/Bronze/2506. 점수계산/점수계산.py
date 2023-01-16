N = int(input())
n_list = input().split('0')
answer_list = []
for item in n_list : 
    answer_list.append(item.count('1'))
result = 0
for num in answer_list :
    result += sum(range(1,num + 1))
print(result)