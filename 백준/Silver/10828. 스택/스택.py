import sys
N = int(sys.stdin.readline())
stack =[]
for _ in range(N):
    order = sys.stdin.readline().split()
    a = order[0]
    if a == 'push': stack.append(order[1])
    elif a == 'pop' : print(stack.pop() if stack else -1)
    elif a == 'size' : print(len(stack))
    elif a == 'empty' : print(0 if stack else 1)
    elif a == 'top' : print(stack[-1] if stack else -1)