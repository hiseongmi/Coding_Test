T = int(input())
numbers = [];
for test_case in range(1, T + 1):
    numbers = list(map(int,input().split()))
    avg = sum(numbers) / len(numbers)
    print("#"+ str(test_case),  round(avg))
