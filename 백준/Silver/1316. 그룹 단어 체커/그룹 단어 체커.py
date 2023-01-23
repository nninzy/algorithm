n = int(input())
cnt = 0
for _ in range(n) :
    word = input()
    new_word = word[0]
    for i in range(1, len(word)) :
        if word[i] != word[i-1] and word[i] not in new_word :
            new_word += word[i]
        elif word[i] != word[i-1] and word[i] in new_word :
            new_word = 1
            break
    if new_word != 1 :
        cnt += 1
print(cnt)