text = input()
for i in range(0, len(text), 10) :
    if i > len(text) - 10 :
        print(text[i:])
    else :
        print(text[i:i+10])