#   프로그래머스 문제 풀이
#   https://school.programmers.co.kr/learn/courses/30/lessons/86052
#   분류 : [월간코드챌린지] 빛의 경로 사이클

def solution(grid):
    #grid = [SL,LR]
    answer = []
    dx = (1,0,-1,0)
    dy = (0,1,0,-1)
    vis = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                if (i,j,d) in vis:
                    continue
                cnt = 0
                nx,ny = i,j
                while (nx,ny,d) not in vis:
                    cnt += 1
                    vis.add((nx,ny,d))
                    if grid[nx][ny] == 'L':
                        d = (d-1) % 4
                    if grid[nx][ny] == 'R':
                        d = (d+1) % 4
                    nx,ny = (nx+dx[d])%len(grid), (ny+dy[d])%len(grid[0])
                answer.append(cnt)
    answer.sort()
    return answer