#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/42583
#   분류 : [스택/큐] 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    second = 0
    completed = []
    in_bridge = [0] * bridge_length
    size = len(truck_weights)
    while len(completed) < size:
        second += 1
        top = in_bridge.pop(0)
        if top != 0:
            completed.append(top)
        if len(truck_weights) > 0: 
            if sum(in_bridge) + truck_weights[0] <= weight:
                in_bridge.append(truck_weights.pop(0))
            else:
                in_bridge.append(0)
    return second