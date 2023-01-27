import sys
import heapq
heap = []
n = int(sys.stdin.readline())
for _ in range(n) :
    num = int(sys.stdin.readline())
    if num == 0 and len(heap) == 0 :
        print(0)
    elif num == 0 :
        print(heap[0][1])
        heapq.heappop(heap)
    else :
        heapq.heappush(heap, (abs(num), num))