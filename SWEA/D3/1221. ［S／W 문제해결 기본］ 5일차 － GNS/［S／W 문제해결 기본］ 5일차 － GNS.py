t = int(input())
for _ in range(t):
    tc, n = input().split()
    arr = input().split()
    d = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt = [0] * 10
    for i in arr:
        cnt[int(d.index(i))] += 1

    print(tc)
    for i in range(10):
        print(' '.join([d[i]] * cnt[i]), end = " ")