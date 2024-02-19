def solution(clothes):
    hash_map = {}
    for c,t in clothes:
        hash_map[t] = hash_map.get(t,0) +1
    
    answer = 1
    for t in hash_map:
        answer *= (hash_map[t] +1)
        
        
    return answer- 1