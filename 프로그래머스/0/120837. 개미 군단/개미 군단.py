def solution(hp):
    j = 5
    c = 3
    a = 1
    count = 0
    while hp > 0:
        if hp >= j:
            hp -= j
            count += 1
        elif c <= hp < j:
            hp -= c
            count += 1
        elif 0 < hp < c:
            hp -= a
            count += 1
        if hp == 0:
            break
    return count
#나누기와 나머지를 이용한다.. 