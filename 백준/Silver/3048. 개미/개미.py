n, m=map(int, input().split())
a=list(input())
b=list(input())
t=int(input())

c=a[::-1]+b # cbadef
for _ in range(t):
    for i in range(len(c)-1):
        if c[i] in a and c[i+1] in b:
            c[i], c[i+1]=c[i+1], c[i]
            # B의 첫번째 요소가 C의 제일 앞에 오는 순간
            if c[i+1] in a[0]: #
                break
print(''.join(c))