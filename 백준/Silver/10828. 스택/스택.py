import sys
N = int(sys.stdin.readline())
stack =[]
for _ in range(N):
    order = sys.stdin.readline().split()
    a = order[0]
    if a == 'push': stack.append(order[1])
    elif a == 'pop' : print(-1 if len(stack) == 0 else stack.pop())
    elif a == 'size' : print(len(stack))
    elif a == 'empty' : print(1 if len(stack) == 0 else 0)
    elif a == 'top' : print(-1 if len(stack) == 0 else stack[-1])