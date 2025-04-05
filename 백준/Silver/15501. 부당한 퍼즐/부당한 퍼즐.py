import sys
input = sys.stdin.readline

n = int(input())
arr = ' '.join(input().split())
result = ' '.join(input().split())
c_arr= arr+ ' ' + arr
rev = ' '.join(arr.split()[::-1])
c_rev =  rev + ' ' + rev

if result in c_arr or result in c_rev:
    print("good puzzle")
else:
    print("bad puzzle")