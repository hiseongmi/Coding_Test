n = int(input())
In = {}
for i in range(n):
    InCar = input()
    In[InCar] = i
out = []
for i in range(n):
    OutCar = input()
    idx = In[OutCar]
    out.append(idx)
result = 0
for i in range(n):
    for j in range(i,n):
        if out[i] > out[j]:
            result += 1
            break

print(result)