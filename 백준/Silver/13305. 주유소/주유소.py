import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = 0
mc = cost[0]
for i in range(n-1):
    if mc > cost[i]: # 원래 기름값보다 가격이 작다면
        mc = cost[i] # 최소값으로 넣어주고
    result += mc * dist[i] # 비용 계산

print(result)