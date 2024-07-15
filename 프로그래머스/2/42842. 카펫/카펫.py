def solution(brown, yellow):
    answer = [0,0]
    arr = []
    block = brown + yellow
    for i in range(1,int(block)+1):
        if block % i == 0:
            if i >= 3:
                arr.append((i, block // i))
                
    for w, h in arr:
        if w < h:
            w, h = h, w
        if yellow == (w-2)*(h-2):
            answer[0] = w
            answer[1] = h
            
    return answer