t = int(input())
for tc in range(1, t + 1):
    a, b, c = map(int, input().split())
    ans = c // min(a, b)
    
    print(f"#{tc}", ans)