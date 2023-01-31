word_matrix = []; max_len = 0
for _ in range(5) :
    text_list = list(input())
    word_matrix.append(text_list)
    if len(text_list) > max_len : max_len = len(text_list)
for i in range(max_len) :
    for j in range(5) :
        try : print(word_matrix[j][i], end = '')
        except : pass
