t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    x = int(''.join(input().split()))
    y = int(''.join(input().split()))
    data = list(map(str,input().split()))
    data += data
    ans = 0
    for i in range(n):
        z = int(''.join(data[i:i+m]))
        if x <= z <= y:
            ans += 1
    print(ans)

