#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/87390
#   분류 : [월간 코드 챌린지 시즌3] n^2 배열 자르기


def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer