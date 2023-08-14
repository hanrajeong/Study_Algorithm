#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/76502
#   분류 : [월간 코드 챌린지 시즌2] 괄호 회전하기
def func(s):
    while True:
        if '()' not in s and '[]' not in s and '{}' not in s:
            break
        s = s.replace('()', '')
        s = s.replace('{}', '')
        s = s.replace('[]', '')
    return 1 if len(s) == 0 else 0
    
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        answer += func(s)
        s = s[1:] + s[0]
    return answer



    