import sys
input = sys.stdin.readline

route = []
for _ in range(36):
    route.append(input().rstrip())
if len(set(route)) != 36:
    print('Invalid')
    exit()
for i in range(1, 36):
    row = abs(ord(route[i][0]) - ord(route[i-1][0]))
    col = abs(int(route[i][1]) - int(route[i-1][1]))
    if (row == 1 and col == 2) or (row == 2 and col ==1):
        continue
    else:
        print('Invalid')
        exit()
        
# 마지막 칸과 첫 번째 칸이 나이트의 이동 규칙에 맞는지 확인
row = abs(ord(route[0][0]) - ord(route[35][0]))
col = abs(int(route[0][1]) - int(route[35][1]))

if (row == 1 and col == 2) or (row == 2 and col == 1):
    print("Valid")
else:
    print("Invalid")