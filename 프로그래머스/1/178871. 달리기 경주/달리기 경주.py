def solution(players, callings):
    dic = {p:i for i, p in enumerate(players)} 
    for i in callings:
        idx = dic[i] #i의 인덱스를 가져와서 그 인덱스를 앞 인덱스와 교환
        players[idx] , players[idx-1] = players[idx-1], players[idx]
        dic[players[idx]] = idx
        dic[players[idx-1]] = idx-1
            
    return players