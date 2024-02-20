from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    ing = deque([0] * bridge_length)
    truck = deque(truck_weights)
    sum_weight = 0
    
    while truck:
        time +=1 
        
        sum_weight -= ing.popleft()
        if sum_weight + truck[0] <= weight:
            sum_weight += truck[0]
            ing.append(truck.popleft())
        else:
            ing.append(0)
    time += bridge_length
    return time