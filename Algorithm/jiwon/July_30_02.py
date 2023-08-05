#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/42628?language=python3
#   분류 : [힙(Heap)] 이중우선순위큐

import heapq

def solution(operations):
    #최소힙
    answer = []
    #최대힙
    answer2 = []
    heapq.heapify(answer)
    heapq.heapify(answer2)
    
    while len(operations)>0:
        a = operations.pop(0)
        num = 0
        if 'I' in a:
            num = int(a.replace('I ', ''))
            heapq.heappush(answer, num)
            heapq.heappush(answer2, -num)
        #최소값 제거
        elif a == "D -1":
            try: 
                heapq.heappop(answer)
                heapq.heappop(answer2)
            except:
                pass
        #최대값 제거
        elif a == "D 1":
            try:
                -heapq.heappop(answer)
                -heapq.heappop(answer2)
            except:
                pass
        if len(answer) == 0 and len(operations) == 0:
            return [0,0]
    
    return [-heapq.heappop(answer2), heapq.heappop(answer)]