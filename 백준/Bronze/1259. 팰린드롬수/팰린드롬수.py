while True :
    answer = 'yes'
    test_num = input()
    if test_num == '0' : break
    start = 0; end = len(test_num) - 1
    while start < end :
        if test_num[start] != test_num[end] :
            answer = 'no'; break
        else :
            start += 1; end -= 1
    print(answer)