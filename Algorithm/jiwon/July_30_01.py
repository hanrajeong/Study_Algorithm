#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/42626
#   분류 : [힙(Heap)] 더 맵게

import heapq 

def solution(scoville, K):
#1) 큐 없이 풀이
#     answer = 0
#     #내림차순정렬
#     scoville.sort(reverse= True)
    
#     while scoville[-1] < K:
#         a = scoville.pop()
#         b = scoville.pop()
#         mix = a + (b*2)
#         scoville.append(mix)
#         scoville.sort(reverse = True)
#         answer +=1
    
#         if len(scoville) ==1 and scoville[0] < K:
#             return -1
        
#     return answer
#2) 큐를 이용한 풀이
    heapq.heapify(scoville)
    answer = 0
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        answer += 1  
    return answer