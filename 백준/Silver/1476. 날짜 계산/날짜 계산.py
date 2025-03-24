e, s, m = map(int, input().split())
r = 1
while True:
    e_r = (r-1) % 15 + 1
    s_r = (r-1) % 28 + 1
    m_r = (r-1) % 19 + 1
    if e_r == e and s_r == s and m_r == m:
        print(r)
        break
    r += 1
    