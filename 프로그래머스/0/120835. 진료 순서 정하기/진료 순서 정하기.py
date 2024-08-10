def solution(emergency):
    answer = []
    n_e = sorted(emergency, reverse = True)
    return [n_e.index(e)+ 1 for e in emergency]