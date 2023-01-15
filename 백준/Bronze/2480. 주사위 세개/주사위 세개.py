num_list = list(map(int, input().split()))
num_dict = {}
for item in num_list :
    if item in num_dict.keys() :
        num_dict[item] += 1
    else :
        num_dict[item] = 1
for key, value in num_dict.items() :
    if value == 3 :
        answer = 10000 + key * 1000
        break;
    elif value == 2 :
        answer = 1000 + key * 100
        break;
    else :
        answer = 100 * max(num_dict.keys())
print(answer)