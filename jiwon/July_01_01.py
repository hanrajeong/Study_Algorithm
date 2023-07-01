#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/12906
#   분류 : [스택/큐] 같은 숫자는 싫어

def solution(arr):
    answer = [arr[0]]
    temp = arr[0]
    for n in arr:
        if temp != n:
            answer.append(n)
        temp = n
    return answer