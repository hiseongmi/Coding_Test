t = int(input())

for tc in range(1, t + 1):
    n = str(input())
    dd = { 'd': 'b', 'b':'d', 'p' : 'q' , 'q':'p'}
    result = ''
    for i in n:
        result += dd[i]
    print(f"#{tc}", result[::-1])