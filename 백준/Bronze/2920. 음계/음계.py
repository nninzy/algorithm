num_list = [1, 2, 3, 4, 5, 6, 7, 8]
input_list = list(map(int, input().split()))
print('ascending' if input_list == num_list else 'descending' if input_list == list(reversed(num_list)) else 'mixed')