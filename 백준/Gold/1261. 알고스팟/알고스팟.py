import heapq
INF = int(1e9)

# 다익스트라 관련 함수
# 1을 가중치로 생각.
def dijkstra():
    dist[0][0] = 0
    heap = [[0, 0]]

    while heap:
        y, x = heapq.heappop(heap)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if maze[ny][nx] == 1:
                    if dist[ny][nx] > dist[y][x] + 1:
                        dist[ny][nx] = dist[y][x] + 1
                        heapq.heappush(heap, [ny, nx])
                else:
                    if dist[ny][nx] > dist[y][x]:
                        dist[ny][nx] = dist[y][x]
                        heapq.heappush(heap, [ny, nx])
# 기본세팅
m, n = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
dist = [[INF] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dijkstra()
print(dist[n - 1][m - 1])