for tc in range(1, 11):
    n = int(input())
    arr = list(input())
    stack = []
    ans = ""

    for i in arr:
        if i == '+':
            while stack:
                ans += stack.pop()
            stack.append(i)
        else:
            ans += i
    while stack:
        ans += stack.pop()
        
    for i in ans:
        if i == '+':
            stack.append(stack.pop()+stack.pop())
        else:
            stack.append(int(i))


    print(f"#{tc}", stack[-1])