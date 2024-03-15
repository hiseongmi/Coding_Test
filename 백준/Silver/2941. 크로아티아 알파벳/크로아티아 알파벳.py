S = input()
c_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]
count = 0
for w in c_list:
	if w in S:
		S = S.replace(w, "m")
print(len(S))