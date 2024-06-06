t = int(input())
for tc in range(1, t+1):
    N = int(input())
    print(f"#{tc}")
    char = ''
    for i in range(N):
        c, k = input().split()
        char += c * int(k)

    for i in range(0, len(char), 10):
        print(char[i:i+10])