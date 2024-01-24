T = int(input())
lists = list(map(int, input().split()))
lists.sort()
print(lists[T // 2])