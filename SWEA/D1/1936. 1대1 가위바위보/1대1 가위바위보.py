A, B = list(map(int, input().split()))
win = {1 : 3, 2 : 1, 3 : 2}
if win[A] == B :
    print('A')
else :
    print('B')