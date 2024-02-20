def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i]) #마지막은안담기니까
    
    answer.append(arr.pop()) #마지막만넣어주기따로
            
    return answer