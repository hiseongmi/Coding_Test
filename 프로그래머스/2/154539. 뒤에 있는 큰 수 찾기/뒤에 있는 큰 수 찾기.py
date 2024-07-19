def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [] # 0 1
    
    for n in range(len(numbers)):
        
        t = numbers[n] #n = 1 t = 1 n = 2 t = 5
        
        while stack and numbers[stack[-1]] < t: #numbers[0] 9 < t 1  numbers[1] 1 < 5
            answer[stack.pop()] = t
            
        stack.append(n)
        
    return answer