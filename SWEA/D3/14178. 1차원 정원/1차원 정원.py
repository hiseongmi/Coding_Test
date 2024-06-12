t = int(input())
for tc in range(1, t+1):
    N, D = map(int, input().split())
    vum = 2 * D + 1
    result = N // vum
    if N % vum != 0:
        result += 1
        
    print(f"#{tc}", result)