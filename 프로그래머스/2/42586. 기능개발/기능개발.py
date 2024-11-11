from collections import deque
def solution(progresses, speeds):
    answer = []
    t = deque([])
    
    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]
        days = 0
        while p < 100:
            p += s
            days += 1
            
        t.append(days)
        
    while t:
        time = t.popleft()
        cnt2 = 1
        while t and t[0] <= time:
            t.popleft()
            cnt2 += 1
        answer.append(cnt2)
        
    return answer