import sys
x = [] ; y = []
for _ in range(3) :
    num_x, num_y = sys.stdin.readline().split()
    x.append(num_x)
    y.append(num_y)
for a in x :
    if x.count(a) == 1 :
        print(a, end = ' ')
for b in y :
    if y.count(b) == 1:
        print(b)