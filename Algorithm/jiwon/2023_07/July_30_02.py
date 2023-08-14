#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/42628?language=python3
#   분류 : [힙(Heap)] 이중우선순위큐

import heapq

def solution(operations):
    answer = []
    answer2 = []
    heapq.heapify(answer)
    heapq.heapify(answer2)
    
<<<<<<< HEAD
    while len(operations) > 0:
        op = operations.pop(0)
        if op[0] == "I":
            heapq.heappush(answer, int(op[1:]))
            heapq.heappush(answer2, -int(op[1:]))
        elif len(answer) == 0 and len(answer2) == 0:
            continue
        elif op == "D 1":
            temp = heapq.heappop(answer2)
            answer.remove(-temp)
        else:
            temp = heapq.heappop(answer)
            answer2.remove(-temp)
    if len(answer) == 0 and len(answer2) == 0:
        return [0, 0]
    answer = [-heapq.heappop(answer2), heapq.heappop(answer)]
    return answer
=======
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
>>>>>>> 778fc1fd32777a282d4fd4652c314c7ddd921b73
