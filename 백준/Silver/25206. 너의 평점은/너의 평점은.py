import sys
input = sys.stdin.readline
avg_g = {"A+": 4.5, "A0" : 4.0, "B+": 3.5, "B0":3.0, "C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
sum_score = 0
sum_grade = 0
for _ in range(20):
	name, score, grade = input().split()
	if grade != "P":
		sum_score += float(score) #소수점임!!
		sum_grade += float(score) * avg_g.get(grade, 0)

print('%.6f' % (sum_grade / sum_score)) #소수점 6자리!!