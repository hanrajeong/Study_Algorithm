#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/42583
#   분류 : [스택/큐] 다리를 지나는 트럭

#큐를 이용한 풀이 (속도 ↓)
from collections import deque

def solution(n,a,b):
    answer = 0
    queue = deque(i for i in range(1,n+1))
        
    while True :
        first = queue.popleft()
        second = queue.popleft()

        if [first,  second] == [a, b] or [first,  second] == [b, a]:
            answer+=1
            break
        if first == a or second == a:
            answer +=1
            queue.append(a)
        elif first == b or second == b:
            queue.append(b)
        else:
            #아무값 second도 됨
            queue.append(first)
    return answer

#이분탐색을 이용한 풀이 (속도 △)
def solution(n,a,b):
    # 발생할 수 있는 최대 라운드 수 계산
    max_round = 0
    while 2 ** max_round < n:
        max_round += 1
    
    # 이진 탐색 적용
    a, b = min(a, b), max(a, b)  # 큰 수, 작은 수 구분
    mid = n // 2  # 중간값
    lower = 0  # 최소값
    upper = n  # 최대값
    
    while True:
        # 탈출 : 두 수가 포함된 라운드가 서로 다를 경우
        if a <= mid and b > mid:
            break
        # 작은 수가 중간값보다 클 경우(라운드에서 두 수가 같은 그룹에 있을 경우)
        elif a >= mid:
            lower = mid
            mid = (mid + upper) // 2
            max_round -= 1 
        # 큰 수가 중간값보다 작거나 같을 경우(라운드에서 두 수가 같은 그룹에 있을 경우)
        elif b <= mid:
            upper = mid
            mid = (mid + lower) // 2
            max_round -= 1
            
    return max_round

# 구현 (속도 ↑)
def solution(n,a,b):
    round = 0 
    while a != b:
        round += 1
        a = (a+1) // 2
        b = (b+1) // 2
    return round