line_num = 5
for n in range(1,line_num+1) :
    line = ''
    for i in range(1,n) :
        line += '+'
    line += '#'
    for j in range(line_num-n,0,-1) :
        line += '+'
    print(line)