total = int(input())
lines = [[] for _ in range(total + 1)]
lnked = int(input())
visited = [False] * (total + 1)
for _ in range(lnked):
    n1, n2 = map(int, input().split())
    lines[n1].append(n2)
    lines[n2].append(n1)

def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        current = stack.pop()
        for adj in lines[current]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
dfs(1)
print(visited.count(True) - 1)