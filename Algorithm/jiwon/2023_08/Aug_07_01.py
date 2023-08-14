#구현 풀이 3개
#https://www.acmicpc.net/problem/1158

from collections import deque
n, k= map(int, input().split())

queue =deque()
answer =[]

for i in range(1,int(n+1)):
  queue.append(i)

while len(queue)>0:
  for _ in range(k-1):
    queue.append(queue.popleft())
  answer.append(str(queue.popleft()))

print('<', ', '.join(answer), '>', sep='')

#https://www.acmicpc.net/problem/1652
n = int(input())
arr = []
row = 0
col = 0
for i in range(n):
  arr.append(input())

for i in range(len(arr)):
  row_temp, col_temp = 0, 0
  for j in range(len(arr)):
    
    #row
    if arr[i][j] == '.':
      row_temp +=1
    else:
      row_temp =0
    if row_temp ==2:
      row+=1
  
    #col
    if arr[j][i] == '.':
      col_temp +=1
    else:
      col_temp =0
    if col_temp ==2:
      col +=1
      
print(row, col)

#https://www.acmicpc.net/problem/1138

n = int(input())
h = list(map(int, input().split()))
ans = [0] * n
for p in range(1, n+1):
    t = h[p-1]
    cnt = 0
    for i in range(n):
        if cnt == t and ans[i] == 0:
            ans[i] = p
            break
        elif ans[i] == 0:
            cnt += 1
print(*ans)

