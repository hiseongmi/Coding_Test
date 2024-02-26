def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            num = numbers[i] * numbers[j]
            print(num)
            if num > answer:
                answer = num
    return answer
#정렬해서 곱하기........... ㅠ