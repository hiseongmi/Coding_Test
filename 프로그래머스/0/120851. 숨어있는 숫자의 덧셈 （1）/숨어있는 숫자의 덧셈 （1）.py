def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer
# isdigit() 및 isalpha() 메서드를 사용하여 숫자와 문자를 구분
#sum(int(i) for i in my_string if i.isdigit()) 