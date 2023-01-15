H, M = map(int,input().split())
M += 15
H -= 1
if M >= 60 :
    H += 1
    M -= 60
H = H+24 if H < 0 else H-24 if H>=24 else H
print(H, M)