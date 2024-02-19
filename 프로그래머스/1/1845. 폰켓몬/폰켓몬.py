def solution(nums):
    list = len(set(nums))
    count = len(nums) / 2
    if int(list) > int(count):
        answer = count
    else: answer = list
    
    return answer