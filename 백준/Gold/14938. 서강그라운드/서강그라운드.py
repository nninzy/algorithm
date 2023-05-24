INF = int(1e9)
# 많은 아이템 습득을 위해 어디 떨어져야 하는가

# 지역 n, 수색범위 m, 길의 개수 r
n, m, r = map(int, input().split())
# 각 지역에서 얻을 수 있는 아이템들 t
t_list = list(map(int, input().split()))
graph = [[INF] * (n+1) for _ in range(n+1)]
answer = 0

# 같은 지점 0 처리
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = min(graph[a][b], l)
    graph[b][a] = min(graph[b][a], l)

# 플로이드 워셜 알고리즘 (모든 경로의 최소거리 구하기)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 시작지점에서 도달지점까지 거리가 수색 범위 이내이면 아이템 회수 (이전 시작 지점들과 비교)
for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            temp += t_list[j - 1]
    answer = max(answer, temp)

print(answer)