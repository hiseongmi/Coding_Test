import sys
input = sys.stdin.readline
n =int(input().rstrip())
arr = []
for _ in range(n):
    arr.append(int(input().rstrip()))
count = 0
cnt = []
ggcd = 0
def gcd(a,b):
    while b:
        a, b = b,  a % b
    return a
for i in range(len(arr)-1):
    cnt.append(int(arr[i+1]-arr[i]))

for i in range(len(cnt)):
    ggcd = gcd(ggcd, cnt[i])
for i in cnt:
    count += (i // ggcd - 1)
print(count)

