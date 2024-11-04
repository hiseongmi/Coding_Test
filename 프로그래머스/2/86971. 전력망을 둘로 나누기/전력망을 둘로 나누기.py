from collections import deque
def bfs(node, a,v):
    q = deque([a])
    cnt = 1
    v[a] = 1
    while q:
        s = q.popleft()
        for i in node[s]:
            if not v[i]:
                v[i] = 1
                cnt += 1
                q.append(i)
    return cnt

def solution(n, wires):
    answer = -1
    arr = []
    for i in wires:
        node = [[] for _ in range(n+1)]
        v = [0] * len(node)
        v[0] = 1
        a, b = i
        for j in wires:
            if i ==j:
                continue
            c, d = j
            node[c].append(d)
            node[d].append(c)
            
        n1 = bfs(node, a,v)
        n2 = n - n1
        arr.append(abs(n1-n2))
        
    answer = min(arr)
    
    return answer