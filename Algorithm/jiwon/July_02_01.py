#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/43162
#   분류 : [DFS/BFS] 네트워크

def solution(n, computers):
    answer = 0
    visitied = [False for _ in range(n)]
    for i in range(n):
        if visitied[i] == False:
            DFS(n, computers, i, visitied)
            answer +=1
    return answer

def DFS(n, computers, j, visitied):
    visitied[j] = True
    for i in range(n):
        if i != j and computers[j][i] == 1:
            if visitied[i] == False:
                DFS(n, computers, i, visitied)
            
    
