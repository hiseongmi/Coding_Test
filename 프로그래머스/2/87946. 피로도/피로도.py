def dfs(k, cnt, d):
    global answer, visited
    
    if cnt > answer:
        answer = cnt
    
    for i in range(len(d)):
        if visited[i] == 0 and k >= d[i][0]:
            visited[i] = 1
            dfs(k - d[i][1], cnt +1, d)
            visited[i] = 0
            
def solution(k, dungeons):
    global answer, visited
    answer = 0
    visited = [0] * len(dungeons)
    
    dfs(k, 0, dungeons)
    
    return answer