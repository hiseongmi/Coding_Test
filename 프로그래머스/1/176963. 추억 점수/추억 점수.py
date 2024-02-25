def solution(name, yearning, photo):
    answer = []
    for a in photo:
        y_sum = 0
        for k in a:
            if k in name:
                y_sum += yearning[name.index(k)]
        answer.append(y_sum)
                
    return answer