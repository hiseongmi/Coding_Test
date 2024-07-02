t = int(input())
for tc in range(1, t+1):
    a = input()
    dic = ['a','e','o','i','u']
    result = ''
    for i in a:
        if not i in dic:
            result += i
    print(f"#{tc}", result)