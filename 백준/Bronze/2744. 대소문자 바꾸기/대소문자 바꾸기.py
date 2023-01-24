word = input()
answer = ''
for i in range(len(word)) :
    if word[i] == word[i].upper() :
        answer += word[i].lower()
    else :
        answer += word[i].upper()
print(answer)