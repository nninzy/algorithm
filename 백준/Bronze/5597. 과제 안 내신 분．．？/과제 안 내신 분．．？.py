import sys
std = list(range(1, 31))
while len(std) != 2 :
    std.remove(int(sys.stdin.readline()))
print(std[0], std[1], sep = '\n')