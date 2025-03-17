import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
mv = [tuple(map(int, input().split())) for _ in range(n)]
mv.sort()
bags = [int(input()) for _ in range(k)]
bags.sort()
que = []
result = 0

for bag in bags:
    while mv and mv[0][0] <= bag:
        heapq.heappush(que, -mv[0][1]) #최소가 최대
        heapq.heappop(mv)
    if que:
        result -= heapq.heappop(que) # 젤 최소 값 출력 -(-99)
print(result)