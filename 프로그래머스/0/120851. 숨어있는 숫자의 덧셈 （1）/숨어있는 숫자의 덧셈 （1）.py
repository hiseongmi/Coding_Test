def solution(my_string):
    answer = 0
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            answer += int(my_string[i])

            
    return answer
# isdigit() 및 isalpha() 메서드를 사용하여 숫자와 문자를 구분