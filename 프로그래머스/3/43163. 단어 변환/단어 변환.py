from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    que = deque()
    que.append([begin,0])
    while que:
        nword, ncnt = que.popleft()
        if nword == target:
            answer = ncnt
            break
        else:
            for i in range(len(words)):
                if visited[i] == 0:
                    cnt = 0
                    for j in range(len(begin)):
                        if nword[j] != words[i][j]:
                            cnt+=1
                            
                    if cnt == 1:
                        ncnt +=1
                        que.append([words[i],ncnt])
                        visited[i] = 1
    return answer