for tc in range(1, 11):
    n = int(input())
    arr = list(input())
    stack = []
    ans = ""
    rank = {'+': 1, '*': 2}
    for i in arr:
        if i == '+' or i == '*':
            if not stack:
                stack.append(i)
            else:
                if rank[stack[-1]] >= rank[i]:
                    while stack and rank[stack[-1]] >= rank[i]:
                        ans += stack.pop()
                stack.append(i)
        else:
            ans += i
    while stack:
        ans += stack.pop()

    for i in ans:
        if i.isdigit():
            stack.append(int(i))
        else:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())

    print(f"#{tc}", stack[-1])