from itertools import combinations

N, M = map(int,input().split())
arr = list(map(int, input().split()))
sum_a = []
diff_a = []
for i in combinations(arr, 3):
	if sum(i) <= M:
		sum_a.append(sum(i))
		diff_a.append(M - sum(i))
        
diff_idx = diff_a.index(min(diff_a))
print(sum_a[diff_idx])
