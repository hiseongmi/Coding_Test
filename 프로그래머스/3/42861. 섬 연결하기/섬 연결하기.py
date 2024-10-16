# Kruskal 알고리즘의 경우, 매 단계에서 가장 비용이 적은 간선을 선택하여 연결합니다. 이때 간선이 선택될 때마다 사이클이 형성되지 않도록 하는 것이 중요합니다.

def find(p, x):
    #p[0] == 0, p[1] ==1
    if p[x] == x:
        return x
    p[x] = find(p, p[x])
    return p[x]

def union(p, a, b):
    rootA = find(p, a)
    rootB = find(p, b)
    
    if rootA < rootB: # 0 < 1
        p[rootB] = rootA  #p[1] = 0 p=[0,0,2,3]
    else:
        p[rootA] = rootB
        
        
def solution(n, costs):
    answer = 0
    #최소비용순으로 정렬
    costs.sort(key = lambda x: x[2])
    
    parent = [i for i in range(n)] #p=[0,1,2,3]
    
    for cost in costs:
        s, e, w = cost
        #사이클이 발생하지 않는다면, 앞에서 연결이 안됐다면
        if find(parent, s) != find(parent, e): # 0 != 1
            #연결해주기
            union(parent, s, e)
            #거리 추가
            answer += w
    
    return answer