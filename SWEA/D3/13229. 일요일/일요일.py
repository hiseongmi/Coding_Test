t= int(input())
S = { "MON":1, "TUE":2, "WED":3, "THU":4, "FRI":5, "SAT":6, "SUN":7 }
for tc in range(1, t+1):
    a = input()
    if a == "SUN":
        print(f"#{tc}", S[a])
    else:
        print(f"#{tc}", 7 - S[a])