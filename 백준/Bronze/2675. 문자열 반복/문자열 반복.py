t = int(input())
for _ in range(t) :
    num_s, text = input().split()
    answer = ''
    for string in text :
        answer += string * int(num_s)
    print(answer)