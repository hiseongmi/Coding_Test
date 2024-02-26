def solution(n):
    answer = 0
    for i in range(1,1000000):
        if i**2 == n:
            answer= 1     
            break
        else:
            answer= 2
    
    return answer

# n ** 0.5는 n의 제곱근을 계산 -> 나머지가 0인지확인후 답추출
