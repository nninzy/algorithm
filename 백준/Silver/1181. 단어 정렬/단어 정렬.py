n = int(input())
len_dict = {}
for _ in range(n) :
    word = input()
    if len(word) in len_dict.keys() :
        if word not in len_dict[len(word)] :
            len_dict[len(word)].append(word)
    else :
        len_dict[len(word)] = [word]
for key in sorted(len_dict.keys()) :
    print(*sorted(len_dict[key]), sep = '\n')