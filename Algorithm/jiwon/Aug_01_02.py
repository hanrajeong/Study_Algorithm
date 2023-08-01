#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/12973
#   분류 : [2017 팁스타운] 짝지어 제거하기

def solution(s):
    answer = 0
    s = list(s)
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
 
    if len(stack) == 0:
        answer = 1
 
    return answer
