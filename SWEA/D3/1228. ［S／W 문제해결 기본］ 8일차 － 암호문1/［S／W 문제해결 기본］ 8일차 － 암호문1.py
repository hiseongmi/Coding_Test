
for tc in range(1, 11):
    N = int(input())
    original = list(map(int, input().split()))
    c = int(input())
    command = list(input().split())

    for i in range(len(command)):
        if command[i] == "I":
            idx = int(command[i+1])
            num = int(command[i+2])
            for j in range(num):
                original.insert(idx + j, int(command[i+3+j]))
    print(f"#{tc}", *original[:10])