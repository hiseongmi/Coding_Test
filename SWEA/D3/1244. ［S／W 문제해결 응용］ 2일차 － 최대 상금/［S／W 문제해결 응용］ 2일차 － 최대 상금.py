t = int(input())
for tc in range(1, t+1):
    s, n = input().split()
    n = int(n)
    num = {s}
    check = set()
    for _ in range(n):
        while num:
            v = num.pop()
            v = list(v)
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    v[i], v[j] = v[j], v[i]
                    check.add(''.join(v))
                    v[i], v[j] = v[j], v[i]
        num, check = check, num
    print(f"#{tc} {max(map(int,num))}")