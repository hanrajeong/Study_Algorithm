#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/1844
#   분류 : [DFS/BFS] 게임 맵 최단거리

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    # n= 세로, m= 가로
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    queue = deque()
    queue.append((0,0))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            #동서남북 움직이는 좌표값
            nx = x + dx[i]
            ny = y + dy[i]
            
            #가로 세로를 벗어나지 않는 범위
            if 0<= nx < n and 0 <= ny < m :
                if maps[nx][ny] == 1:
                    # 거리를 1씩 계속 추가
                    maps[nx][ny] =  maps[x][y] +1
                    
                    queue.append((nx, ny))

    if maps[n-1][m-1] >1:
        return maps[n-1][m-1]
    else:
        return -1 

                
