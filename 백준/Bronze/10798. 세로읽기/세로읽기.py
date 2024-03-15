s = [input() for i in range(5)]
for i in range(15): #줄 최대 15까지
	for j in range(5):
		if i < len(s[j]):
			print(s[j][i],end="")