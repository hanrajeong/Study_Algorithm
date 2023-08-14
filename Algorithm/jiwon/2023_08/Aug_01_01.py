#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/68645
#   분류 : [월간 코드 챌린지 시즌2] 삼각달팽이

def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            #down
            if i % 3 == 0:
                x += 1
                
            #right
            elif i % 3 == 1:
                y += 1
                
            #up
            elif i % 3 == 2:
                x -= 1
                y -= 1        
            res[x][y] = num
            num += 1
            
    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer