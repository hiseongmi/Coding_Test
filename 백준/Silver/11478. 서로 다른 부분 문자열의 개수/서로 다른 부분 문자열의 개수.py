import sys
input = sys.stdin.readline
s = str(input().rstrip()) #123
str = set()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        str.add(s[i:j])

print(len(str))

