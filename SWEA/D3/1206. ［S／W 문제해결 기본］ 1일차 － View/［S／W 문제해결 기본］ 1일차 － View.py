for tc in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    r = 0
    for i in range(2, n - 2):
        if lst[i - 1] < lst[i] and lst[i + 1] < lst[i] and lst[i - 2] < lst[i] and lst[i + 2] < lst[i]:
            m_v = max(lst[i - 1], lst[i + 1], lst[i - 2], lst[i + 2])
            m = lst[i] - m_v
            r += m

    print(f"#{tc}", r)
