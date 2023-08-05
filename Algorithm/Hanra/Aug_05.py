# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    answer = 0
    maxW = 0
    maxH = 0
    for size in sizes:
        if size[0] < size[1]:
            temp = size[0]
            size[0] = size[1]
            size[1] = temp
        maxW = max(maxW, size[0])
        maxH = max(maxH, size[1])
    answer = maxW * maxH
    return answer