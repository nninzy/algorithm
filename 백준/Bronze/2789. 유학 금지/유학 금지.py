string = input()
blocked = 'CAMBRIDGE'
for alp in string :
    if alp not in blocked :
        print(alp, end = '')