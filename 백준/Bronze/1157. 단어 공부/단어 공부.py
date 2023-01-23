text = input().upper()
text_dict = {}
for word in text :
    if word in text_dict.keys() :
        text_dict[word] += 1
    else :
        text_dict[word] = 1
max_cnt = max(text_dict.values())
max_list = []
for key, value in text_dict.items() :
    if value == max_cnt :
        max_list.append(key)
print('?' if len(max_list) > 1 else max_list[0])