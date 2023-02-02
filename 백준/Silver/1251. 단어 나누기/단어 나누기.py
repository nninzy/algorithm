word = input()
new_words = []
for i in range(1, len(word)-1):
    for j in range(i+1,len(word)):
        wd1 = word[:i]
        wd2 = word[i:j]
        wd3 = word[j:]
        new_wd = wd1[::-1] + wd2[::-1] + wd3[::-1]
        new_words.append(new_wd)
print(sorted(new_words)[0])