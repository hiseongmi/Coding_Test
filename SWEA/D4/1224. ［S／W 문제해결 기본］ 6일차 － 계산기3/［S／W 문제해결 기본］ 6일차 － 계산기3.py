for tc in range(1, 11):
    n = int(input())
    arr = list(input())
    stack = []
    ans = ""
    rank = {'+': 1, '*': 2, '(': 0}
    r_rank = {'+': 1, '*': 2, '(': 3}

    for i in arr:
        if i.isdigit():
            ans += i
        else:
            if not stack:
                stack.append(i)
            elif i in '+*(':
                if rank[stack[-1]] >= r_rank[i]:
                    ans += stack.pop()
                stack.append(i)
            else:
                while stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()

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
